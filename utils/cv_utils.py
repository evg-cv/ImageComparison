import cv2

from settings import STANDARD_HEIGHT, STANDARD_WIDTH


def standardize_image(frame):

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    _, _, img_v = cv2.split(img_hsv)
    norm_v = cv2.normalize(img_v, None, 0, 255, cv2.NORM_MINMAX)
    equ_v = cv2.equalizeHist(norm_v)
    blur_v = cv2.medianBlur(equ_v, 5)

    # frame_gray = cv2.cvtColor(blur_v, cv2.COLOR_BGR2GRAY)
    frame_resize = cv2.resize(blur_v, (STANDARD_WIDTH, STANDARD_HEIGHT), interpolation=cv2.INTER_CUBIC)
    # cv2.imshow("standard image", blur_v)
    # cv2.waitKey()

    return frame_resize


if __name__ == '__main__':

    standardize_image(frame="")
