def saveAnnotatedSample(self, path):
        skel2 = self.crop2D()
        skel2 = skel2.reshape(-1, 3)
        for i, pt in enumerate(skel2):
            skel2[i] = Camera.to2D(pt)
        print 'current camera option={}'.format(Camera.focal_x)

        skel = self.skel
        skel.shape = (-1,3)

        dm = self.norm_dm.copy()
        dm[dm == Camera.far_point] = 0
        ax = fig.add_subplot(121)
        img = dm.copy() 
        img = img - img.min()
        img *= 255/img.max()
        for pt in skel2:
            cv2.circle(img, (pt[0], pt[1]), 2, (255,0,0), -1)
        cv2.imwrite(path, img) 
