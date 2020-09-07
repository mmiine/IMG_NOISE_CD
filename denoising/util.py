from skimage.restoration import estimate_sigma
import numpy as np
from matplotlib import pyplot as plt


def est_sigma(img):
    mc = False
    if img.ndim > 2:
        mc = True
    sigma = estimate_sigma(img, multichannel= mc)
    sigma=np.average(sigma)
    print("Estimated sigma = %.2f" % sigma)
    return sigma

def dft(img):
    #dft = cv.dft(np.uint8(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(np.abs(dft_shift))
    return magnitude_spectrum , dft_shift

def idft(img):
    f_ishift = np.fft.ifftshift(img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)
    return img_back


def noise_detect(noisy, smooth = None):
    noisy = noisy[:,:,0]
    if smooth == None:
        smooth = noisy[0:30,0:30]
    plt.figure()
    plt.subplot(221), plt.imshow(noisy, cmap='gray')
    plt.title('Noisy Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(smooth, cmap='gray')
    plt.title('Smooth Part'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.hist(noisy.ravel(), 256, [0, 256])  # ; plt.show()
    plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.hist(smooth.ravel(), 256, [0, 256])  # ; plt.show()
    plt.title('Estimated Noise Distribution'), plt.xticks([]), plt.yticks([])
    plt.show()
