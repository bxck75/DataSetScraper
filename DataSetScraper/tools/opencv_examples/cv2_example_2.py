def find_center(self, name, frame, mask, min_radius):
        if name not in self.pts:
            self.pts[name] = deque(maxlen=self.params['tracking']['buffer_size'])

        # find contours in the mask and initialize the current (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # only proceed if at least one contour was found
        if len(cnts) &gt; 0:
            # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))

            # only proceed if the radius meets a minimum size
            if radius &gt; min_radius:
                # draw the circle and centroid on the frame, then update the list of tracked points
                cv2.circle(frame, center, int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                self.pts[name].appendleft(center)
                smooth_points = 8
                return (int(np.mean([self.pts[name][i][0] for i in range(min(smooth_points, len(self.pts[name])))])),
                        int(np.mean([self.pts[name][i][1] for i in range(min(smooth_points, len(self.pts[name])))]))), radius
        return None, None 
