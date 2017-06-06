# Mean Shift Segmentation implementation
# Credits to http://www.chioka.in/meanshift-algorithm-for-the-rest-of-us-python/
import cv2
from numpy import array, zeros, linalg, exp, floor


def mean_shift_segmentation(image, kernel_size=3, bandwidth=16, max_iterations=1000):
    segmentor = MeanShiftSegmentor(image, kernel_size, bandwidth)

    for i in range(0, max_iterations):
        limits = segmentor.image.shape
        image_prev = segmentor.image
        for x in range(segmentor.kernel_dist, limits[0]+segmentor.kernel_dist):
            for y in range(segmentor.kernel_dist, limits[1]+segmentor.kernel_dist):
                window = segmentor.neighbours([x, y])
                segmentor.image[x, y] = segmentor.weighted_sum(window)

        if linalg.norm(image_prev - segmentor.image) < 0.0000001:
            break

    return segmentor.remove_padding(segmentor.image)


class MeanShiftSegmentor(object):
    image = array
    kernel_size = int
    kernel = array
    kernel_dist = int

    def __init__(self, image: array, kernel_size: int, bandwidth: int):

        self.kernel_dist = int(floor(float(kernel_size) / 2))
        self.image = self.__border_padding(image)
        self.image = cv2.normalize(self.image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
        self.kernel_size = kernel_size
        self.kernel = self.__create_kernel(kernel_size, bandwidth)

    def weighted_sum(self, window: array):
        weighted_sum = 0
        limits = window.shape
        for x in range(0, limits[0]):
            for y in range(limits[1]):
                weighted_sum += self.kernel[x, y] * window[x, y]
        return weighted_sum

    def neighbours(self, point):
        x = point[0]
        y = point[1]
        return self.image[x - self.kernel_dist:x + self.kernel_dist, y - self.kernel_dist:y + self.kernel_dist]

    def __create_kernel(self, kernel_size: int, bandwidth: int):
        mat = zeros(shape=(kernel_size, kernel_size))
        mean = zeros(shape=(2, 1))
        mean[:] = self.kernel_dist

        for x in range(0, kernel_size):
            for y in range(0, kernel_size):
                mat[x, y] = self.__gauss([x, y], mean, bandwidth)

        return mat / linalg.norm(mat)

    def __gauss(self, point, mean, bandwidth) -> float:
        distance = linalg.norm(mean - point)
        return exp(-0.5 * (distance / bandwidth) ** 2)

    def __border_padding(self, image):
        return cv2.copyMakeBorder(image, top=self.kernel_dist, bottom=self.kernel_dist, left=self.kernel_dist,
                                  right=self.kernel_dist,
                                  borderType=cv2.BORDER_REPLICATE)

    def remove_padding(self, image):
        return image[self.kernel_dist:image.shape[0] - self.kernel_dist,
               self.kernel_dist:image.shape[1] - self.kernel_dist]
