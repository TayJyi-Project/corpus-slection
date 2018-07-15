import os
import math
import librosa
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


directory = '../storage/kp-select/'
dirs = os.listdir(directory)
# must be sorted 
dirs = sorted(dirs)

# read audio in
audio_data = []
for doc in dirs:
    if doc.endswith('.wav'):
        fpath = os.path.join(directory, doc)
        temp, _ = librosa.load(fpath)
        audio_data.append(temp)

# feature extraction with mfcc
mfcc_data = []
for audio in audio_data:
    mfcc = librosa.feature.mfcc(audio, 44100, n_mfcc=13)
    mfcc_data.append(mfcc.mean(axis=1))

# t-SNE to 2D plane
tsne_mfcc = TSNE(n_components=2).fit_transform(mfcc_data) # perplexity=30, n_iter=10000

# extract coordinate dataset 
x, y = tsne_mfcc.T

# k-means clustering
k_means = KMeans(n_clusters=30, random_state=0).fit(tsne_mfcc)

# select leaders
# print(k_means.cluster_centers_)
center = k_means.cluster_centers_
group = k_means.labels_
setlen = len(x)
for i in range(0, 30):
    minlen = 1e9+10
    for j in range(0, setlen):
        if group[j] == i and minlen > math.sqrt( (x[j]- center[group[j]][0])**2 + (y[j] - center[group[j]][1]) ** 2):
            minlen = math.sqrt( (x[j]- center[group[j]][0])**2 + (y[j] - center[group[j]][1]) ** 2)
            minlenidx = j
    # print("leader of group_{0} is chunk_{1}.wav".format(i, minlenidx+1))
    print(os.path.join(directory, dirs[minlenidx]))

plt.scatter(x, y)
for i in range(len(x)):
    plt.annotate(str(k_means.labels_[i])+','+str(i+1), (x[i], y[i]))
plt.show()