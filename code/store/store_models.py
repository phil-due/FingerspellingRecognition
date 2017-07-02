from sklearn.externals import joblib

from classification.pipe import get_pipe
from daq.DatasetGenerator import DatasetGenerator

dir_dataset = '../../resource/dataset/tm'
model_file = '../../resource/models/model_hog_asl.pkl'
# Reads dataset, trains models and stores them on file system
data, labels = DatasetGenerator.load_data_sign('../../resource/models/descriptors_pixel.pkl',
                                               '../../resource/models/labels.pkl')


pipe = get_pipe()
pipe.fit(data, labels.ravel())
joblib.dump(pipe, model_file)
