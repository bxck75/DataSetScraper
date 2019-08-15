def draw_circle(img, radius, x, y,thinkness=1):
    """
    Render circle
    :param img    : Canvas 
    :param radius : Radius of the circle
    :param x      : (x, y) is the center of the circle graph on the canvas
    :param y      : (x, y) is the center of the circle graph on the canvas
    """
    ############################################################
    #                  Write your code here!                   #
    ############################################################

    # cv2.circle(img, (x, y), radius, (20, 215, 20), thinkness)
    cv2.circle(img, (int(x+radius/1.5),int(y+radius/1.5)),80, (20, 215, 1), thinkness)
    ############################################################
    #                           End                            #
    ############################################################ 

