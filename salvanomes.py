from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("C:/Users/moham/OneDrive/Desktop/MAC0329-145-2021-Lista1-3515900")]
names = []
for name in onlyfiles:
    i = 0
    while (name[i] != '_'):
        i += 1
    names.append(name[0:i])
for name in names:
    print(name + ',')