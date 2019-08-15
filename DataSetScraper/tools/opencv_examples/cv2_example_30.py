def draw_images(self, frame, hsv, mask_ball, mask_arena, arena_center, arena_ring_radius=None):
        self.draw_history(frame, 'ball')
        self.draw_history(frame, 'arena')
        if arena_ring_radius is not None:
            cv2.circle(frame, arena_center, arena_ring_radius, (0, 128, 255), 2)
        return frame

        #rgbs = cv2.split(frame)
        #hsvs = cv2.split(hsv)

        #cv2.imshow(Hue, hsvs[0])
        #cv2.imshow(Mask ball, mask_ball)
        #cv2.imshow(Mask arena, mask_arena)
        #cv2.imshow(Frame, frame)
        #cv2.waitKey(1)

        #cv2.imshow(Red, rgbs[0])
        #cv2.imshow(Green, rgbs[1])
        #cv2.imshow(Blue, rgbs[2])
        #cv2.imshow(Saturation, hsvs[1])
        #cv2.imshow(Value, hsvs[2])
        #cv2.waitKey(1) 
