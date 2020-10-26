import cv2 as cv
import numpy as np
from skimage.util import random_noise, img_as_float


def gaussian(image, mean=0, sigma=0.01):
    gaussian_noise = np.random.normal(mean, sigma, image.shape) * 255
    dumb = np.clip(gaussian_noise*0.5 + image, 0.0, 255.0)
    return dumb


def salt_pepper(image, prob=0.01):
    uniform_noise = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)

    cv.randu(uniform_noise, 0, 255)
    ret, impulse_noise1 = cv.threshold(uniform_noise, 255 - prob * 255, 255, cv.THRESH_BINARY)
    impulse_noise1 = (impulse_noise1).astype(np.uint8)

    cv.randu(uniform_noise, 0, 255)
    ret, impulse_noise2 = cv.threshold(uniform_noise, 255 - prob * 255, 255, cv.THRESH_BINARY)
    impulse_noise2 = (impulse_noise2).astype(np.uint8)

    if np.ndim(image) > 2:
        impulse_noise1 = np.dstack([impulse_noise1] * 3)
        impulse_noise2 = np.dstack([impulse_noise2] * 3)

    dumb = cv.add(image, impulse_noise1)
    dumb = cv.subtract(dumb, impulse_noise2)

    return dumb


def poisson(image):
    dumb=random_noise(image,mode='poisson')
    return dumb


def speckle(image):
    dumb=random_noise(image,mode='speckle')
    '''mult_noise = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    cv.randn(mult_noise,0,0.3)
    dumb = mult_noise * image + image
    '''
    return dumb


def white(image):
    white_noise = np.random.random(image.shape) * 255
    dumb = np.clip(white_noise*0.4 + image, 0.0, 255.0)
    return dumb


def periodic(image):
    periodic_wave = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    sin0 = np.linspace(0, 2*image.shape[0], image.shape[0])
    sin0 = np.reshape(sin0, (image.shape[0],1))
    sin0 = (np.sin(2*np.pi*sin0/360)+1)/2*255
    for i in range(image.shape[1]):
        for j in range(image.shape[0]):
            periodic_wave[j,i] = sin0[j]

    dumb = periodic_wave*0.5 + image
    return dumb


def quantization(image):
    quant = np.random.uniform(0.0 , 255.0, image.size)
    quant = np.reshape(quant, (image.shape[0], image.shape[1]))
    dumb = np.clip(quant * 0.4 + image, 0.0,255.5)
    return dumb


def gamma(image, shape = 0.1, scale = 1.0):
    gamma = np.random.gamma(shape, scale, image.shape)
    print(gamma)
    gamma= img_as_float(gamma)
    print(gamma)
    print(gamma.shape)
    dumb = np.clip(gamma*255 + image, 0.0, 255.0)
    return dumb


def poisson_gaussian(image):
    gaussian_noise = np.random.normal(0, 0.01, image.shape) * 255
    dumb = poisson(image)+0.02*gaussian_noise
    dumb = np.clip(dumb, 0.0, 255.5)
    return dumb