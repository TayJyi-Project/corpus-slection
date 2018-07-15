import os
import random

audpath = '../storage/kp3/'
dirs = sorted(os.listdir(audpath))
print(sorted(random.sample(dirs,30)))

