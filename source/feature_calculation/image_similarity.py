from source.feature_calculation.image_feature import ImageFeature
from scipy.spatial import distance


image_feature_detector = ImageFeature()


def calculate_distance_between_features(test_frame_path, origin_frame_path):

    test_feature = image_feature_detector.get_feature_from_image(img_path=test_frame_path)
    origin_feature = image_feature_detector.get_feature_from_image(img_path=origin_frame_path)

    dist = distance.euclidean(origin_feature, test_feature)

    return dist


if __name__ == '__main__':

    dist = calculate_distance_between_features(test_frame_path="/media/mensa/Data/Task/ImageComparison/data/1003.jpg",
                                               origin_frame_path="/media/mensa/Data/Task/ImageComparison/data/4.jpg")
    print(dist)

