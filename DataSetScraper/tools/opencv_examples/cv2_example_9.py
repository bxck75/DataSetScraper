def do_draw(self, event, x, y, flags, param):
        draw_vals = {1: 100, 2: 0}

        if event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
            self.drawing = 0
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = 1
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.drawing = 2
        elif self.drawing != 0:
            cv2.circle(self.img, (x, y), 5, draw_vals[self.drawing], -1) 
