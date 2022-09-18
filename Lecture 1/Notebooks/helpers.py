import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN = 0
MAX = 255

plt.rcParams['figure.figsize'] = [12, 8]

def minmax(value):
    if value < MIN:
        return MIN
    elif value > MAX:
        return MAX
    else:
        return value

def contrast_brightness(image, alpha, beta):
    new_image = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if len(image.shape) == 2:
                new_image[y, x] = minmax(alpha * image[y, x] + beta)
            else:
                for c in range(image.shape[2]):
                    new_image[y, x, c] = minmax(alpha * image[y, x, c] + beta)
    return new_image

def show_histogram(img, channel=0):
    hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
    plt.plot(hist)
    plt.grid()
    plt.show()
    
def show_histograms(img):
    for channel, color in zip(range(img.shape[2]), ['r', 'g', 'b']):
        hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.grid()
    plt.show()