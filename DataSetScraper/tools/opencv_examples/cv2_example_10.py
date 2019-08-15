def draw_circle(event,x,y,flags,param):
    global drawing,drawing1
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing1 = True
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
        if drawing1 == True:
            cv2.circle(img,(x,y),5,(0,255,0),-1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
    if event == cv2.EVENT_RBUTTONUP:
        drawing1 = False
    #print (drawing) 
