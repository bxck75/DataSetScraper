def execute_GoodFeaturesToTrack(proxy,obj):
	'''
	https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
	'''
	try: img=obj.sourceObject.Proxy.img.copy()
	except: img=cv2.imread(__dir__+'/icons/freek.png')

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	corners = cv2.goodFeaturesToTrack(gray,obj.maxCorners,obj.qualityLevel,obj.minDistance)
	corners = np.int0(corners)

	for i in corners:
		x,y = i.ravel()
		cv2.circle(img,(x,y),3,255,-1)

	obj.Proxy.img = img 
