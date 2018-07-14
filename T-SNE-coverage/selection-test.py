import os
import librosa
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def get_scaled_tsne_embeddings(features, perplexity, iteration):
    embedding = TSNE(n_components=2,
                     perplexity=perplexity,
                     n_iter=iteration).fit_transform(features)
    scaler = MinMaxScaler()
    scaler.fit(embedding)
    return scaler.transform(embedding)

counter = 0
directory = '../storage/kp-select/'
audio_data = []
dirs = os.listdir(directory)
dirs = sorted(dirs)
for doc in dirs:
    if doc.endswith('.wav'):
        fpath = os.path.join(directory, doc)
        temp, _ = librosa.load(fpath)
        audio_data.append(temp)


mfcc_data = []
for audio in audio_data:
    mfcc = librosa.feature.mfcc(audio, 44100, n_mfcc=13)
    mfcc_data.append(mfcc.mean(axis=1))


tsne_mfcc = TSNE(n_components=2, perplexity=30, n_iter=10000).fit_transform(mfcc_data)
x, y = tsne_mfcc.T

plt.scatter(x, y)
for i in range(len(x)):
    plt.annotate(str(i+1), (x[i], y[i]))
plt.show()
