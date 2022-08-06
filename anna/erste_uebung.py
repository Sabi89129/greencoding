'''
from codecarbon import EmissionsTracker

tracker = EmissionsTracker(tracking_mode = 'process')
tracker.start()
# COMPREHENSIVE LISTS
# GPU Intensive code goes here
newlist = [x for x in range(10000000)]
print(' Hallo Informatica feminale 2022')

tracker.stop()
'''


'''
from codecarbon import EmissionsTracker
tracker = EmissionsTracker(tracking_mode = 'process')
tracker.start()
# COMPREHENSIVE LISTS
# GPU Intensive code goes here
numbers = []
for x in range(50000000):
    if x % 2 == 0:
        numbers.append(x**2)
print(' Hallo Informatica feminale 2022')

tracker.stop()
'''

from codecarbon import EmissionsTracker
tracker = EmissionsTracker(tracking_mode = 'process')
tracker.start()
# COMPREHENSIVE LISTS
# GPU Intensive code goes here
newlist = [x for x in range(50000000) if x % 2 == 0]
print("hi")

tracker.stop()
