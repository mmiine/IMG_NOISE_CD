import cv2 as cv
import numpy as np
from bm3d import bm3d_rgb
from skimage.restoration import denoise_wavelet
from .util import est_sigma
from time import time


def median(img, kernel=3):
    dumb = cv.medianBlur(img, kernel)
    return dumb


def nl_means(img,sw=21,h=3):
    dumb = cv.fastNlMeansDenoisingColored(img,searchWindowSize=sw,h=h)
    return dumb


def wavelet(img, method = ' ', sigma = None):
    '''
    :param img:
    :param method: 'visu' or 'bayes'
                    standard is visu
    :param sigma:
    :return:
    '''

    if sigma == None:
        sigma = est_sigma(img)

    if method == 'bayes':
        dumb = denoise_wavelet(img, multichannel=True, convert2ycbcr=True,
                           method='BayesShrink', mode='soft',
                           rescale_sigma=True)

    else:
        dumb = denoise_wavelet(img, multichannel=True, convert2ycbcr=True,
                               method='VisuShrink', mode='soft',
                               sigma=sigma, rescale_sigma=True)

    return dumb


def bilateral(img,d=5,ss=30,sc=30):
    '''

    :param img:
    :param d:
    :param ss:
    :param sc:
    :return:
    '''
    dumb = cv.bilateralFilter(img, d, ss, sc)
    return dumb


def bm3d(img, sigma = None ):
    if sigma == None:
        sigma = est_sigma(img)
        if sigma < 4:
            sigma **= 2
            print("Used sigma = %.2f" %sigma)
    try:
        tic = time()
        dumb = bm3d_rgb(img, sigma)
        tock = time()
        print("Execute time = %.2f" % (tock - tic), "s")
    except:
        print("Something went wrong, trying different method.")
        tic = time()
        dumb = cv.xphoto.bm3dDenoising(img)
        tock = time()
        print("Execute time = %.2f" % (tock - tic), "s")
    dumb = np.clip(dumb, 0.0, 255.0).astype('uint8')
    return dumb


def band_reject(rgb, low, high = 'inf'):
    image = cv.cvtColor(rgb, cv.COLOR_BGR2YCrCb)
    img = image[:,:,0]
    (col, row) = img.shape

    dft = np.fft.fft2(img)
    D0 = low
    if high == 'inf':
        D1 = max(col,row)+1
    else: D1 = high

    u1 = np.arange(0, col / 2 + 1, 1)
    u2 = np.arange(-col / 2 + 1, 0, 1)
    u = np.concatenate((u1, u2))
    v1 = np.arange(0, row / 2 + 1, 1)
    v2 = np.arange(-row / 2 + 1, 0, 1)
    v = np.concatenate((v1, v2))

    U, V = np.meshgrid(u, v)
    D = np.sqrt(np.power(U, 2) + np.power(V, 2))

    H = np.ones(img.shape)
    for i in range(col):
        for j in range(row):
            if D[j, i] > D0 and D[j, i] < D1:
                H[i, j] = 0
    G = np.multiply(H, dft)
    img_back = np.fft.ifft2(G)
    img_back = np.real(img_back)
    img_back = np.clip(img_back,0.0,255.0)
    image[:,:,0] = img_back
    dumb = cv.cvtColor(image, cv.COLOR_YCrCb2BGR)


    return dumb

