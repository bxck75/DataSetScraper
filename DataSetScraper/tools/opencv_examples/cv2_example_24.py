def side_intersect(self, image, contours, row, markup=True):
         Find intersections to both sides along a row 
        if markup:
            cv2.line(image, (0, row), (image.shape[1], row), (0, 0, 255), 1)

        cnt_l, col_l = self.find_intersect(image, contours, row, -1)
        if markup and cnt_l is not None:
            cv2.drawContours(image, [contours[cnt_l]], -1, (0, 255, 255), -1)
            cv2.circle(image, (col_l, row), 4, (0, 255, 0), 2)

        cnt_r, col_r = self.find_intersect(image, contours, row, 1)
        if markup and cnt_r is not None:
            cv2.drawContours(image, [contours[cnt_r]], -1, (255, 255, 0), -1)
            cv2.circle(image, (col_r, row), 4, (0, 255, 0), 2)

        return (cnt_l, col_l), (cnt_r, col_r) 
