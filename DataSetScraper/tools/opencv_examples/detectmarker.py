def detectmarker(image):
    grayscale = getgrayimage(image)
    mkradius = getapproxmarkerradius(grayscale) # approximate marker radius
    marker = cv2.resize(MARKER, (mkradius*2, mkradius*2)) # resize the marker
    
    #template matching
    matched = cv2.matchTemplate(grayscale, marker, cv2.TM_CCORR_NORMED) #returns float32
        
    #detect 4 greatest values
    markerposarray = []
    for i in range(4):
        (minval, maxval, minloc, maxloc) = cv2.minMaxLoc(matched)
        markerposarray.append(tuple(map(lambda x: x+mkradius, maxloc))) 
        cv2.circle(matched, maxloc, mkradius, (0.0), -1) #ignore near the current minloc
        
    return markerposarray 
