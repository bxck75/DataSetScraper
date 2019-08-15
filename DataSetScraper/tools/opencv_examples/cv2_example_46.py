def draw_gt_market(test_image, joints, save_image):
    image = cv2.imread(test_image)
    # draw joints in green spots
    for j in xrange(len(joints) / 2):
        cv2.circle(image, (joints[j * 2], joints[j * 2 + 1]), 2, (0, 255, 0), 1)
    # draw torso in yellow lines
    p1 = [0, 0, 5]
    p2 = [1, 14, 10]
    for j in xrange(len(p1)):
        cv2.line(image, (joints[p1[j] * 2], joints[p1[j] * 2 + 1]), (joints[p2[j] * 2], joints[p2[j] * 2 + 1]),
                 (0, 255, 255), 1)
    # draw left part in pink lines
    p1 = [14, 13, 12, 13, 10, 9]
    p2 = [13, 12, 11, 10, 9, 8]
    for j in xrange(len(p1)):
        cv2.line(image, (joints[p1[j] * 2], joints[p1[j] * 2 + 1]), (joints[p2[j] * 2], joints[p2[j] * 2 + 1]),
                 (255, 0, 255), 1)
    # draw right part in blue lines
    p1 = [1, 2, 3, 2, 5, 6]
    p2 = [2, 3, 4, 5, 6, 7]
    for j in xrange(len(p1)):
        cv2.line(image, (joints[p1[j] * 2], joints[p1[j] * 2 + 1]), (joints[p2[j] * 2], joints[p2[j] * 2 + 1]),
                 (255, 0, 0), 1)
    cv2.imwrite(save_image, image) 
