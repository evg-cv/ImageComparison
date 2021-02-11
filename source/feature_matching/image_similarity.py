import cv2
import numpy as np

from utils.cv_utils import standardize_image
from settings import FLANN_INDEX_KDTREE
from matplotlib import pyplot as plt


def match_two_images(test_frame_path, origin_frame_path):

    origin_frame_ = cv2.imread(test_frame_path)
    origin_frame = standardize_image(frame=origin_frame_)

    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(origin_frame, None)

    # bf = cv2.BFMatcher()
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    lowe_ratio = 0.89

    frame = cv2.imread(origin_frame_path)
    test_frame = standardize_image(frame=frame)
    kp2, des2 = orb.detectAndCompute(test_frame, None)

    print(origin_frame_path)
    good = []

    # matches = bf.match(des1, des2)

    # print("length of match:", len(matches))
    # matches = sorted(matches, key=lambda x: x.distance)
    # sum_dist = 0
    # for match in matches[:10]:
    #     sum_dist += match.distance
    #     print(match.distance)
    # print("average distance:", sum_dist / 10)

    # matches = bf.knnMatch(des1, des2, k=2)
    # Apply ratio test
    # for m, n in matches:
    #     if m.distance < lowe_ratio * n.distance:
    #         good.append([m])
    # img3 = cv2.drawMatchesKnn(origin_frame, kp1, test_frame, kp2, good, None, flags=2)
    # print(len(good))

    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)

    for i, (m, n) in enumerate(matches):

        if m.distance < lowe_ratio * n.distance:

            good.append(m)

    print(len(good))

    draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), flags=0)

    img3 = cv2.drawMatchesKnn(origin_frame, kp1, test_frame, kp2, good, None, **draw_params)

    plt.imshow(img3, ), plt.show()

    return len(good)


if __name__ == '__main__':

    match_two_images(test_frame_path=None, origin_frame_path=None)
