import os
import json
import sys

from settings import IMG_SITE_DIR, SM_THRESH
from source.manage_database.write_data import ManageDatabase
from source.ssim.image_similarity import compare_two_images


def estimate_similarity(test_frame_path):

    test_path = os.path.join(IMG_SITE_DIR, test_frame_path)

    origin_frame_paths = database_manager.read_data()

    similarity_ratio = []
    for origin_frame_path in origin_frame_paths:

        if origin_frame_path == test_frame_path:
            continue

        origin_path = os.path.join(IMG_SITE_DIR, origin_frame_path[0])

        diff, sm_ratio = compare_two_images(test_frame_path=test_path, origin_frame_path=origin_path)
        similarity_ratio.append(sm_ratio)

    # max_similarity = max(similarity_ratio)
    sorted_frame = sorted(zip(origin_frame_paths, similarity_ratio), key=lambda y: y[1], reverse=True)

    ret_val = []
    new_rect = {}
    for path, similarity in sorted_frame:

        if similarity > SM_THRESH:
            new_rect["similarity"] = path[0]
            new_rect["factor"] = similarity
            ret_val.append(new_rect)
    # if max_similarity > 0.3:
    #     max_index = similarity_ratio.index(max_similarity)
    #     max_frame = origin_frame_paths[max_index]
    #
    #     ret_val = [max_frame, max_similarity]
    #
    # else:
    #     ret_val = []

    return ret_val


if __name__ == '__main__':

    database_manager = ManageDatabase()

    try:
        frame_path = sys.argv[1]
    except Exception as e:
        print(e)
        sys.exit(1)
    # frame_path = "1.jpg"

    sm = estimate_similarity(test_frame_path=frame_path)

    # Generate some data to send to PHP
    result = {'similarity': sm}

    # Send it to stdout (to PHP)
    print(json.dumps(result))
    # print(frame_path)
