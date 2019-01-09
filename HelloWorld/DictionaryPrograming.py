# Dictionaries are ordered set of data

# Sets are un ordered set of data , do not contains duplicates

# creating a dictionary below myDict = {K:V}

myDict = {1: "One",
          2: "Two",
          3: "Three",
          4: "Four",
          5: "Five"}

# print(myDict)
#
# print(myDict[3])
#
# # deleting an entry in a dictionary is using a del myDict[K] - deletes the entry corresponding to key
#
# del myDict[2]
#
# print(myDict)
#
# # Clearing the contents of the dictionary
#
# myDict.clear()
#
# print(myDict)
#
# # extract the items which does not exist
#
# print(myDict[1])

# Use get and put functions
# used an integer key causes a problem to quit while loop

while True:
    _key = int(input("Please enter the key to get the value : "))
    _value = myDict.get(_key)
    if _key != 'quit':
        print("""Value for the :{0} 
entered is :{1}""".format(_key, _value))
    else:
        break