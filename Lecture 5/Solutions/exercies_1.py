from time import sleep
import numpy as np
import cv2

########################################################################################
TEMPLATE_IMAGE_PATH = '../Data/biker.png'
VIDEO_IMAGE_PATH = '../Data/slow_traffic_small.mp4'

START_FRAME = 114
END_FRAME = 630
X, Y, W, H = 597, 183, 40, 30

HSV_RANGE = np.array([0., 50., 180.]), np.array([30., 150., 240.])

TERMINATION_CITERIA = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 2)
########################################################################################

template_image = cv2.imread(TEMPLATE_IMAGE_PATH)
template_image_hsv = cv2.cvtColor(template_image, cv2.COLOR_BGR2HSV)
template_image_mask = cv2.inRange(template_image_hsv, HSV_RANGE[0], HSV_RANGE[1])
template_image_hist = cv2.calcHist([template_image_hsv], [0, 1], template_image_mask, [180, 255], [0, 180, 0, 255])
template_image_hist = cv2.normalize(template_image_hist, template_image_hist, 0, 255, cv2.NORM_MINMAX)

cap = cv2.VideoCapture(VIDEO_IMAGE_PATH)
frame_index = 0

track_window = (X, Y, W, H)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_mask = cv2.inRange(hsv_frame, HSV_RANGE[0], HSV_RANGE[1])

    if START_FRAME <= frame_index and frame_index <= END_FRAME:
        backProjection = cv2.calcBackProject([hsv_frame], [0, 1], template_image_hist, [0, 180, 0, 255], 1)

        ret, track_window = cv2.meanShift(backProjection, track_window, TERMINATION_CITERIA)
        print(f'Frame {frame_index}: {ret}, {track_window}')
        
        x, y, w, h = track_window
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
    
    
    cv2.imshow(f'Video', frame)
    cv2.imshow(f'Video Mask', frame_mask)
    
    frame_index += 1
    
    sleep(0.02)
    if cv2.waitKey(1) == ord('q'):
        break
