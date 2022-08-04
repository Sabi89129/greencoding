from codecarbon import EmissionsTracker

tracker = EmissionsTracker(tracking_mode = 'process')
tracker.start()
# COMPREHENSIVE LISTS
# GPU Intensive code goes here
numbers = []
for x in range(1000000000):
    if x % 2 == 0: 
        numbers.append(x**2)

print(' Hallo Informatica feminale 2022')

tracker.stop()


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 