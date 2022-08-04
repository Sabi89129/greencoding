from codecarbon import EmissionsTracker
import numpy as np

# Summenberechnung als for-schleife implementiert
# Aufgabe: Generiere ein array=[0,1,....,n] und summiere die Elemente
def langsam(n):
    summe = 0
    for i in range(n):
        summe = summe+i
    print("Langsame Berechnung: ",summe)

# Summenberechnung mit np.sum implementiert
# Aufgabe: Generiere ein np.array=[0,1,....,n] und summiere die Elemente mit np.sum
def schnell(n):
    pass()


# main
tracker = EmissionsTracker()
tracker.start()

# GPU Intensive code goes here
loops = 1000000000

langsam(loops)
#schnell(loops)
tracker.stop()

print(' Hallo Informatica feminale 2022 - FERTIG')
