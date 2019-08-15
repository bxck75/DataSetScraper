def draw(event, x, y, flags, param):
	global drawing, ix, iy, shape, canvas, brush

	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if shape == 1:
				cv2.circle(canvas, (x, y), pencil, color, -1)
			elif shape == 2:
				cv2.circle(canvas, (x, y), brush, color, -1)
			elif shape == 3:
				cv2.circle(canvas, (x, y), eraser, (255, 255, 255), -1)
			elif shape == 5:
				cv2.rectangle(canvas, (ix, iy), (x, y), color, -1)
			elif shape == 6:
				cv2.circle(canvas, (x, y), calc_radius(x, y), color, -1)
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if shape == 1:
			cv2.circle(canvas, (x, y), pencil, color, -1)
		elif shape == 2:
			cv2.circle(canvas, (x, y), brush, color, -1)
		elif shape == 3:
			cv2.circle(canvas, (x, y), eraser, (255, 255, 255), -1)
		elif shape == 4:
			cv2.line(canvas, (ix, iy), (x, y), color, pencil)
		elif shape == 5:
			cv2.rectangle(canvas, (ix, iy), (x, y), color, -1)
		elif shape == 6:
			cv2.circle(canvas, (x, y), calc_radius(x, y), color, -1) 
