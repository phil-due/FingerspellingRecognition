from numpy import mean, std
from sklearn.model_selection import cross_val_score

from classification.pipe import get_pipe
from daq.fileaccess import get_paths_asl
from daq.gendata import load_data_sign, gendata_sign

n_data = 2500
data, labels = gendata_sign(get_paths_asl("../../resource/dataset/fingerspelling5/dataset5/"))

model = get_pipe()
results = cross_val_score(model, data, labels.ravel(), cv=6)
print("Accuracy: " + str(mean(results)) + "(+/- " + str(std(results)))