import time
import os
from os.path import abspath
from lru_cache import *

# Original running complexity was n**2

start_time = time.time()
file_directory = os.path.dirname(abspath(__file__))
f = open(os.path.join(file_directory, 'names_1.txt'), 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(os.path.join(file_directory, 'names_2.txt'), 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
cache_1 = lru_cache.LRUCache(len(names_1))
cache_2 = lru_cache.LRUCache(len(names_2))

for index in range(len(names_1)):
    cache_1.set(names_1[index], True)
    cache_2.set(names_2[index], True)

    if cache_1.get(names_2[index]):
        duplicates.append(names_2[index])
    if cache_2.get(names_1[index]):
        duplicates.append(names_1[index])

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(sorted(duplicates))}\n\n")
print(f"runtime: {end_time - start_time} seconds")


"""
## Stretch optimization for low RAM device
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
names = []
for name_1 in names_1:
    names.append(name_1)

for name_2 in names_2:
    if name_2 in names:
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
 """
