import cv2

# from tracker.MeanShiftSegmentor import mean_shift_segmentation
from daq.DatasetGenerator import gendata_sign
from daq.ImReader import get_paths_tm
from daq.preprocessing.PreProcessing import preprocess_img


def main():

    img, _ = gendata_sign(get_paths_tm(),
                          sample_size=1)

    img.reshape(shape=(100, 120))

    cv2.imshow('image', img)
    cv2.waitKey(1)
    img = preprocess_img(img)
    cv2.imshow("after preprocessing", img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    exit(0)


main()
