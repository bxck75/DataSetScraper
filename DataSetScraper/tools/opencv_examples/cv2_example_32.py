def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(int)  # ????????????????????????16?reshape?2??array
    fx, fy = flow[y, x].T  # ???????????????
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)  # ????????????2*2???
    lines = np.int32(lines + 0.5)  # ????????????
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))  # ???????????????
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)  # ???????????????????
    return vis 