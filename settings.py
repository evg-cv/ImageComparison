import os

from utils.folder_file_manager import make_directory_if_not_exists


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGIN_IMG_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'data', 'origin_images'))
TEST_IMG_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'data', 'test_images'))
MODEL_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'data', 'model'))
MYSQL_CREDENTIAL_PATH = os.path.join(CUR_DIR, 'utils', 'mysql_credential.json')

INCEPTION_URL = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
# IMG_SITE_DIR = os.path.join(CUR_DIR, 'images', 'original')
IMG_SITE_DIR = os.path.join('/opt', 'lampp', 'htdocs', 'server', 'images', 'original')
FLANN_INDEX_KDTREE = 0
STANDARD_WIDTH = 800
STANDARD_HEIGHT = 600
SM_THRESH = 0.8
