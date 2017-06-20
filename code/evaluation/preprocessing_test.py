import random

import cv2

from daq.dataset.fileaccess import read_image
from daq.dataset.preprocessing import preprocess, extract_descriptor

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u",
           "v", "w", "x", "y"]

letter = str(random.choice(letters))
example_image_file = "../../resource/dataset/tm/" + letter + str(
    random.choice(range(1, 40))) + ".tif"
# read image
img = read_image(example_image_file)

cv2.imshow('image', img)
cv2.waitKey(5)
img = preprocess(img)
cv2.imshow("after prefiltering", img)
cv2.waitKey(10000)

descriptor = extract_descriptor(img)
print("Descriptor: \n" + str(descriptor))
print("dim: \n" + str(len(descriptor)))
cv2.destroyAllWindows()
exit(0)
