import os
import numpy as np
from sklearn.manifold import TSNE
from pydub import AudioSegment
import matplotlib.pyplot as plt

audioPath = '../storage/kp3/'
X = []
items = sorted(os.listdir(audioPath))

for item in items:
    X.append(AudioSegment.from_file(audioPath + item).get_array_of_samples())
# get min len
minlen = 1e9+10
for i in X:
    if len(i) < minlen:
        minlen = len(i)

for i in range(len(X)):
    X[i] = X[i][:minlen]

X_embedded = TSNE(n_components=2, init='pca').fit_transform(X)
X_embedded = np.array(X_embedded)
x, y = X_embedded.T

plt.scatter(x, y)
bnd = 2000000
plt.xlim(-bnd,bnd)
plt.ylim(-bnd,bnd)
plt.show()