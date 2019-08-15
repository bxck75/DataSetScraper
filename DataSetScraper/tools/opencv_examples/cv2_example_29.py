def vis_pose(normed_vec):
    import depth 
    origin_pt = np.array([0,0,depth.DepthMap.invariant_depth])
    vec = normed_vec.copy()*50.0
    vec.shape = (-1,3)

    offset_x = Camera.center_x - depth.DepthMap.size2[0]/2
    offset_y = Camera.center_y - depth.DepthMap.size2[1]/2
    
    img = np.ones((depth.DepthMap.size2[0], depth.DepthMap.size2[1]))*255
    img = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_GRAY2BGR)
    for idx, pt3 in enumerate(vec):
        pt = Camera.to2D(pt3+origin_pt)
        pt = (pt[0]-offset_x, pt[1]-offset_y)
        cv2.circle(img, (int(pt[0]), int(pt[1])),2, (255,0,0), -1)
    return img 
