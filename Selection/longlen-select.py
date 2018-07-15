import os
import random
from pydub import AudioSegment

audpath = '../storage/kp3/'
dirs = sorted(os.listdir(audpath))

signals = []
for cur in dirs:
    sound = AudioSegment.from_file(os.path.join(audpath, cur))
    signals.append([len(sound.get_array_of_samples()), cur])
signals = sorted(signals, reverse=True)
z = [x[1] for x in signals[:30]]
z = sorted(z)
print(z)
