import pickle
import time
from threading import Thread

def Loop():
    while 1:
        time.sleep(1)
Thread(target=Loop).start()

# bild, (x, y)
MAP = [
    [0, (96, 0)],
    [0, (96*2, 0)],
    [0, (96*3, 0)],
    [0, (96*4, 0)],
    [0, (96*5, 0)],
    [0, (96*3, 96*3)]
]


file = open(__file__[:-13]+'Map.dat', 'wb')
pickle.dump(MAP, file)
file.close()
print('File updated successfully')