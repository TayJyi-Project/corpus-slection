# ref: https://stackoverflow.com/questions/46757852/adding-silent-frame-to-wav-file-using-python

import os
import re
from pydub import AudioSegment

audir = [
            '/home/ecl/corpus-slection/storage/hawa-kmeans-kp-kmeans/',
            '/home/ecl/corpus-slection/storage/hawa-long-kp-long/',
            '/home/ecl/corpus-slection/storage/hawa-random-kp-random/',
            '/home/ecl/corpus-slection/storage/hawa-short-kp-short/',
            '/home/ecl/corpus-slection/storage/kp-kmeans/',
            '/home/ecl/corpus-slection/storage/kp-long/',
            '/home/ecl/corpus-slection/storage/kp-random/',
            '/home/ecl/corpus-slection/storage/kp-short/'
        ]

maxlen = 0
for i in range(len(audir)):
    items = os.listdir(audir[i])
    for item in items:
        sound = AudioSegment.from_file(audir[i] + item)
        maxlen = max(maxlen, len(sound))

# print(maxlen)


for i in range(len(audir)):
    items = os.listdir(audir[i])
    for item in items:
        sound = AudioSegment.from_file(audir[i] + item)
        delta = maxlen - len(sound)
        # print(delta)
        silent = AudioSegment.silent(duration=delta, frame_rate=44100)
        origin = AudioSegment.from_file(audir[i] + item)
        normaud = silent + origin
        normaud.export(audir[i] + item, format='wav')