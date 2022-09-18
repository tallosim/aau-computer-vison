import cv2
import numpy as np
from matplotlib import pyplot as plt

MIN = 0
MAX = 255

plt.rcParams['figure.figsize'] = [12, 8]

def show_histograms(img):
    if len(img.shape) == 2:
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist)
    else:
        for channel, color in zip(range(img.shape[2]), ['r', 'g', 'b']):
            hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
            plt.plot(hist, color=color)
    plt.grid()
    plt.show()
    

# source: https://stackoverflow.com/a/43346070
def genarate_gussian_kernel(kernel_radius, sigmaX=1, sigmaY=1):
    ax = np.linspace(-kernel_radius, kernel_radius, kernel_radius * 2 + 1)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-0.5 * (np.square(xx) / np.square(sigmaX) + np.square(yy) / np.square(sigmaY)))
    
    return kernel / np.sum(kernel)

def create_mean_kernel(kernel_radius):
    return np.ones((kernel_radius * 2 + 1, kernel_radius * 2 + 1)) / (kernel_radius * 2 + 1) ** 2

def erosion(image, kernel_radius, iterations=1):
    kernel = create_mean_kernel(kernel_radius)
    return cv2.erode(image, kernel, iterations=iterations)

def dilation(image, kernel_radius, iterations=1):
    kernel = create_mean_kernel(kernel_radius)
    return cv2.dilate(image, kernel, iterations=iterations)

def opening(image, kernel_radius, iterations=1):
    kernel = create_mean_kernel(kernel_radius)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iterations)

def closing(image, kernel_radius, iterations=1):
    kernel = create_mean_kernel(kernel_radius)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iterations)

