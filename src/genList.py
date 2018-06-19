
import os
import re

audir = ['/home/ecl/corpus-slection/storage/kp1/','/home/ecl/corpus-slection/storage/kp2/','/home/ecl/corpus-slection/storage/kp3/',
         '/home/ecl/corpus-slection/storage/hawa2kp1/','/home/ecl/corpus-slection/storage/hawa2kp2/','/home/ecl/corpus-slection/storage/hawa2kp3/']

outdir = ['kp1', 'kp2', 'kp3', 'hawa2kp1', 'hawa2kp2', 'hawa2kp3']

for i in range(len(audir)):
    print(audir[i])
    buff = []
    items = os.listdir(audir[i])
    for item in items:
        buff.append(audir[i] + item)
    buff = sorted(buff)
    with open('./audList/' + outdir[i], 'w') as fp:
        for bla in buff:
            fp.write(bla + '\n')