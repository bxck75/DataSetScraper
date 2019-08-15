def brush_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, r,g,b,radius

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  # start to draw when L button down
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True and mode == True:
            cv2.circle(img, (x,y), radius, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False     # end drawing when L button up
        if mode == True:
            cv2.circle(img, (x,y), radius, (b, g, r), -1)



# Create a black image, a window 
