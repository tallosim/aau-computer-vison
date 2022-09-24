import cv2
import numpy as np
import glob

TL = 50
TH = 200

filenames = glob.glob('../Data/Test016/*.tif')
filenames.sort()

images = [cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in filenames]

background_image = np.median(np.array(images), axis=0).astype(np.uint8)
image_index = 0

while True:
    image = images[image_index].copy()

    foreground = np.abs(image - background_image)
    foreground_mask = cv2.inRange(foreground, TL, TH).astype(np.uint8)

    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    red_mask = np.stack([np.zeros_like(foreground_mask), np.zeros_like(foreground_mask), foreground_mask], axis=2)
    image = cv2.addWeighted(image, 0.5, red_mask, 0.5, 0)
    
    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Output", 800, 600)
    cv2.imshow("Output", image)

    key = cv2.waitKey(0)
    if key == 113 or key == 27: # q or Esc
        break
    if key == 124: # Right arrow
        image_index = min(image_index + 1, len(images)-1)
    if key == 123:  # Left arrow
        image_index = max(image_index - 1, 0)
        
