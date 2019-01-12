# Shelve is a persistent dictionary
# Modifying items in a shelve
# Values are pickled before it is written and unpickle before read
import shelve

list1 = ["Varinder", "Arun", "Prasanta"]

with shelve.open('receipe') as recepies:
    recepies["list1"] = list1
    for item in recepies.keys():
        print(recepies[item])

