def draw_joints(test_image, joints, save_image):
    image = cv2.imread(test_image)
    joints = np.vstack((joints, (joints[8, :] + joints[11, :])/2))
    # bounding box
    bbox = [min(joints[:, 0]), min(joints[:, 1]), max(joints[:, 0]), max(joints[:, 1])]
    # draw bounding box in red rectangle
    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 2)
    # draw joints in green spots
    for j in xrange(len(joints)):
        cv2.circle(image, (joints[j, 0], joints[j, 1]), 5, (0, 255, 0), 2)
    # draw torso in yellow lines
    torso = [[0, 1], [1, 14], [2, 14], [5, 14]]
    for item in torso:
        cv2.line(image, (joints[item[0], 0], joints[item[0], 1]), (joints[item[1], 0], joints[item[1], 1]), (0, 255, 255), 2)
    # draw left part in pink lines
    lpart = [[1, 5], [5, 6], [6, 7], [5, 14], [14, 11], [11, 12], [12, 13]]
    for item in lpart:
        cv2.line(image, (joints[item[0], 0], joints[item[0], 1]), (joints[item[1], 0], joints[item[1], 1]), (255, 0, 255), 2)
    # draw right part in blue lines
    rpart = [[1, 2], [2, 3], [3, 4], [2, 14], [14, 8], [8, 9], [9, 10]]
    for item in rpart:
        cv2.line(image, (joints[item[0], 0], joints[item[0], 1]), (joints[item[1], 0], joints[item[1], 1]), (255, 0, 0), 2)
    cv2.imwrite(save_image, image) 
