import cv2
import numpy as np

cap = cv2.VideoCapture('../Data/slow_traffic_small.mp4')

ret, current_frame = cap.read()
current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, next_frame = cap.read()
    next_frame_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(current_frame_gray, next_frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    for y in range(0, current_frame.shape[0], 10):
        for x in range(0, current_frame.shape[1], 10):
            flow_at_point = np.int32(np.round(flow[y, x] * 5))
            line_start = (x, y)
            line_end = (x+flow_at_point[0], y+flow_at_point[1])
            cv2.line(current_frame, line_start, line_end, (0, 0, 255), 1)
    
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Output", 800, 600)
    cv2.imshow("Output", current_frame)

    current_frame = next_frame
    current_frame_gray = next_frame_gray

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
