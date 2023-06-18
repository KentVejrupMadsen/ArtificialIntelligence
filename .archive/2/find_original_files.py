# -*- coding: utf-8 -*-
from os import walk
from os.path import join

import cv2

path_to_search = r"C:\DataSets\Work in progress\symbol-image-dataset\dataset"


def traverse():
    global path_to_search

    for root, dirs, files in walk(path_to_search, topdown=False):
        for f in files:
            #print('current : ', f)
            full_path = join(root, f)

            try:
                image = cv2.imread(full_path)

                if not (image.shape is None):
                    height = image.shape[0]
                    width = image.shape[1]

                    if not (width == 500) or not (height == 500):
                        print("outside range: ", full_path)

            except Exception:
                print("Error loading file.")


if __name__ == '__main__':
    traverse()
