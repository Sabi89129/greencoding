from codecarbon import EmissionsTracker

tracker = EmissionsTracker(tracking_mode = 'process')
tracker.start()
# COMPREHENSIVE LISTS
# GPU Intensive code goes here
# Aufgabe: Optimiere, sodass die Anzahl der Funktionsaufrufe minimiert wird
def square(num):
    return num**2

squares = []
for i in range(1000000000):
    squares.append(square(i))

print(' Hallo Informatica feminale 2022')

tracker.stop()