import os
import random

import cv2


def read_image(path):
    try:
        img = cv2.imread(path, 1)
        if img is None:
            raise FileNotFoundError("Couldn't find: " + path)
    except Exception:
        print("Exception on reading file :" + path)

    return img


def read_letters(img_file_paths, sample_size, letters):
    random.shuffle(letters)
    letter_imgs = {}
    for class_, letter in enumerate(letters, 1):
        letter_imgs[letter] = []
        try:
            path_sel = random.sample(img_file_paths[letter], sample_size)
        except ValueError:
            print("Too many samples requested for [" + letter + "], taking all: " + str(len(path_sel)))

        for sel_samples, path in enumerate(path_sel):
            img = read_image(path)
            letter_imgs[letter].append(img)

    return letter_imgs


def getpaths_asl(dir_dataset='../../resource/dataset/fingerspelling5/dataset5/',
                 sets=None, ):
    if sets is None:
        sets = ["A", "B", "C", "D", "E"]

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y"]
    paths = {}

    for dir_letter in alphabet:
        paths[dir_letter] = [str]
        for dir_set in sets:
            fnames = [f for f in os.listdir(dir_dataset + dir_set + "/" + dir_letter) if 'color' in f]
            for fname in fnames:
                paths[dir_letter].append(dir_dataset + dir_set + "/" + dir_letter + "/" + fname)

    return paths


def getpaths_tm(dir_dataset='../../../resource/dataset/tm'):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y"]
    paths = {}

    for dir_letter in alphabet:
        paths[dir_letter] = [str]
        i = 1
        while os.path.isfile(dir_dataset + '/' + dir_letter + str(i) + '.tif'):
            paths[dir_letter].append(dir_dataset + '/' + dir_letter + str(i) + '.tif')
            i += 1

    return paths
