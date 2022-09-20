import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_histograms(img, ax=None):
    if ax is None:
        fig, ax = plt.subplots(1, 1)
    
    min_value = np.min(img)
    max_value = np.max(img)
    
    if len(img.shape) == 2:
        hist = cv2.calcHist([img], [0], None, [256], [min_value, max_value])
        ax.plot(hist)
    else:
        for channel, color in zip(range(img.shape[2]), ['r', 'g', 'b']):
            hist = cv2.calcHist([img], [channel], None, [256], [min_value, max_value])
            ax.plot(hist, color=color)
    ax.grid()
    return ax
