from array import array
from codecarbon import EmissionsTracker
import numpy as np
import random

# Generieren eines Arrays mit n Zufallszahlen als for-schleife implementiert
def langsame_zufallszahlen(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(0,100))
    return arr

# Generieren eines Arrays mit n Zufallszahlen mit np.random.randint implementiert
def schnelle_zufallszahlen(n):
    pass



# main
tracker = EmissionsTracker()
tracker.start()

# GPU Intensive code goes here
loops = 100000000
langsame_zufallszahlen(loops)
#schnelle_zufallszahlen(loops)
tracker.stop()

print(' Hallo Informatica feminale 2022 - FERTIG')
