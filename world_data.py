import pickle
import time
from threading import Thread

def Loop():
    while 1:
        time.sleep(1)
Thread(target=Loop).start()

# bild, (x, y)
MAP = [
    [0, (0, 0)],
    [0, (96, 0)]
]


file = open(__file__[:-13]+'Map.dat', 'wb')
pickle.dump(MAP, file)
file.close()
print('File updated successfully')