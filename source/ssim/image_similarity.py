import os
import glob
import ntpath
import numpy as np
import cv2

from skimage.metrics import structural_similarity as ssim
from settings import STANDARD_HEIGHT, STANDARD_WIDTH, CUR_DIR


def compare_two_images(test_frame_path, origin_frame_path):

    # compute the mean squared error and structural similarity
    # index for the images
    test_frame = cv2.imread(test_frame_path)
    # test_frame = cv2.resize(test_frame, (STANDARD_WIDTH, STANDARD_HEIGHT))
    origin_frame = cv2.imread(origin_frame_path)
    # origin_frame = cv2.resize(origin_frame, (STANDARD_WIDTH, STANDARD_HEIGHT))
    origin_frame = cv2.resize(origin_frame, (test_frame.shape[1], test_frame.shape[0]))
    m = mse(test_frame, origin_frame)
    s = ssim(test_frame, origin_frame, multichannel=True)

    return m, s


def mse(image_a, image_b):

    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are

    return err


if __name__ == '__main__':

    test_img_path = os.path.join(CUR_DIR, 'data', 'test_images', 'FL-257-801-004.png')
    origin_frame_paths = glob.glob(os.path.join(CUR_DIR, 'data', 'origin_images', "*.png"))

    for origin_path in origin_frame_paths:

        _, similarity = compare_two_images(test_frame_path=test_img_path, origin_frame_path=origin_path)
        print("origin_image:{}, similarity: {}".format(ntpath.basename(origin_path), similarity))
