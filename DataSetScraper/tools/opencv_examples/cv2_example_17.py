def _get_mask(self, scan, slide, series):
		img, s, o, origShape = scan
		mask = np.zeros((origShape[1], origShape[2]))
		nodules = self._nodule_info[series]
		for nodule in nodules:
			iid, z, edges = nodule
			z = int((z - o[2])/s[2])
			if z == slide:
				if edges.shape[0] &gt; 1:
					cv.fillPoly(mask, [edges], 255)
				else:
					#It's a small nodule. Make a circle of radius 3mm
					edges = np.squeeze(edges)
					center = tuple(edges)
					radius = max(3.0/s[0], 3.0/s[1])
					cv.circle(mask, center, int(radius+1), 255, -1)

		if img.shape[1] != origShape[1] or img.shape[2] != origShape[2]:
			mask = imu.resize_2d(mask, (img.shape[1], img.shape[2]))
		return mask 
