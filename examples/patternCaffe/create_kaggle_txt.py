import numpy as np
import os
 
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR_PATTERN_TRAIN = os.path.abspath(os.path.join(CURRENT_DIR, '../../data/patternCaffe/pattern_sets/train'))
DATA_DIR_PATTERN_TEST = os.path.abspath(os.path.join(CURRENT_DIR, '../../data/patternCaffe/pattern_sets/test'))
DATA_DIR_PRODUCT_TRAIN = os.path.abspath(os.path.join(CURRENT_DIR, '../../data/patternCaffe/product_sets/train'))
DATA_DIR_PRODUCT_TEST = os.path.abspath(os.path.join(CURRENT_DIR, '../../data/patternCaffe/product_sets/test'))
TXT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../../data/patternCaffe/'))

 
pattern_images_train = [image for image in os.listdir(DATA_DIR_PATTERN_TRAIN)]
pattern_images_test = [image for image in os.listdir(DATA_DIR_PATTERN_TEST)]
product_images_train = [image for image in os.listdir(DATA_DIR_PRODUCT_TRAIN)]
product_images_test = [image for image in os.listdir(DATA_DIR_PRODUCT_TEST)]
 
pattern_train = pattern_images_train[:int(len(pattern_images_train))]
pattern_test = pattern_images_test[:int(len(pattern_images_test))]
 
product_train = product_images_train[:int(len(product_images_train))]
product_test = product_images_test[:int(len(product_images_test))]
 
with open('{}/train.txt'.format(TXT_DIR), 'w') as f:
    for image in pattern_train:
        f.write('{} 0\n'.format(image))
    for image in product_train:
        f.write('{} 1\n'.format(image))
 
with open('{}/test.txt'.format(TXT_DIR), 'w') as f:
    for image in pattern_test:
        f.write('{} 0\n'.format(image))
    for image in product_test:
        f.write('{} 1\n'.format(image))