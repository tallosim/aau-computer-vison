from matplotlib import pyplot as plt
import cv2

plt.rcParams['figure.figsize'] = [12, 8]

def show_histograms(img, max_height=None):
    if len(img.shape) == 2:
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist)
    else:
        for channel, color in zip(range(img.shape[2]), ['r', 'g', 'b']):
            hist = cv2.calcHist([img], [channel], None, [256], [0, 256])
            plt.plot(hist, color=color)
    
    if max_height:
        plt.ylim(0, max_height)
    
    plt.grid()
    plt.show()