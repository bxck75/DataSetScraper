def init_mask(self, event, x, y, flags, param):
		self._thickness = 3 # The thickness in drawing;
		self._WHITE = [255, 255, 255] # Pure white;

		# Draw a point on the image;
		if event == cv2.EVENT_RBUTTONDOWN:
			if self._drawing == True:
				cv2.circle(self.img, (x, y), self._thickness, self._WHITE, -1)
				self.mask[y-self._thickness:y+self._thickness, x-self._thickness:x+self._thickness] = self._SHADOW
				self._shadow_seed = self.img[y-self._thickness:y+self._thickness, x-self._thickness:x+self._thickness].copy()

		elif event == cv2.EVENT_RBUTTONUP:
			if self._drawing == True:
				self._drawing = False
				self._drawn = True
				cv2.circle(self.img, (x, y), self._thickness, self._WHITE, -1) 
