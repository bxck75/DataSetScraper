def execute_BlobDetector(proxy,obj):

	try: img=obj.sourceObject.Proxy.img.copy()
	except: img=cv2.imread(__dir__+'/icons/freek.png')

	im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	im=255-im
	im2 = img

	params = cv2.SimpleBlobDetector_Params()

	params.filterByArea = True
	params.minArea = obj.Area

	params.filterByConvexity = True
	params.minConvexity = obj.Convexity/200


	# Set up the detector with default parameters.
	detector = cv2.SimpleBlobDetector_create(params)
	
	# Detect blobs.
	keypoints = detector.detect(im)
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	if not obj.showBlobs:
		im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		obj.Proxy.img = im_with_keypoints
		
		for k in keypoints:
			(x,y)=k.pt
			x=int(round(x))
			y=int(round(y))
#			cv2.circle(im,(x,y),4,0,5)
			cv2.circle(im,(x,y),4,255,5)
			cv2.circle(im,(x,y),4,0,5)
			im[y,x]=255
			im[y,x]=0
		obj.Proxy.img = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
		
	else:
		for k in keypoints:
			(x,y)=k.pt
			x=int(round(x))
			y=int(round(y))
			cv2.circle(im2,(x,y),4,(255,0,0),5)
			cv2.circle(im2,(x,y),4,(0,0,0),5)
			im2[y,x]=(255,0,0)
			im2[y,x]=(0,0,0)
		obj.Proxy.img = im2 
