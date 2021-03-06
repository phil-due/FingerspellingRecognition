import numpy as np
from sklearn.externals import joblib


class EstimatorVideo:
    model = None
    trained = False
    iterations = 0
    n_letters = 24

    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.trained = True
        self.votes = np.zeros(shape=self.n_letters)

    def predict(self):
        if np.max(self.votes) > self.iterations * 0.75:
            class_ = int(np.argmax(self.votes))
            self.votes = np.zeros(shape=self.n_letters)
            self.iterations = 0
            return class_
        else:
            return -1

    def stack_descr(self, descriptor):
        self.votes[int(self.model.predict(descriptor.astype(np.float))) - 1] += 1
        self.iterations += 1
