import sys
import argparse
import cv2 as cv
from denoising.addnoise import (gaussian, salt_pepper)
from denoising.denoise import (bm3d, wavelet)


parser = argparse.ArgumentParser('Test an image')
parser.add_argument(
    '--mode', choices=['gaussian', 'salt_pepper', 'bm3d', 'wavelet'], help='iqa gaussian, salt & pepper, bm3d')
parser.add_argument('--path', required=True, help='image path')
args = parser.parse_args()


if __name__ == "__main__":
    '''
    test for two noise types and one denoise method
    '''
    path = args.path
    mode = args.mode
    im = cv.imread(path)
    if im is None:
        print("please input correct image path!")
        sys.exit(0)
    elif mode == 'gaussian':
        dumb = gaussian(im)
    elif mode == 'salt_pepper':
        dumb = salt_pepper(im)
    elif mode == 'bm3d':
        dumb = bm3d(im)
    elif mode == 'wavelet':
        dumb = wavelet(im)

    cv.imshow(str(mode),dumb)
    cv.waitKey(0)
    cv.destroyAllWindows()
