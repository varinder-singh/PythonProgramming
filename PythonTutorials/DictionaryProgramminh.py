# create a dictionary
# use get(), keys(), values(), items() operations on the dictionary Object

fruit = {"apple": "good for cider",
         "orange": "sweet citrus fruit",
         "lemon": "citrus fruit",
         "banana": "full of potassium"}

# while True:
#     _key = input("Please enter the key to be sought for in the dictionary : ")
#     if _key == 'quit':
#         break
#     else:
#         print(fruit.get(_key, "{} is not in the dictionary.".format(_key)))
#
# for name in fruit:
#     print(fruit[name])
# # use keys()
# fruit_keys = fruit.keys()
#
# print(fruit_keys)
#
# fruit["tomato"] = "not good with ice-cream"
#
# print(fruit_keys)
#
# # use values(), apparently it is not optimized
# print(fruit.values())
#
# # Use items(), show the dictionary as a list and elements as a tuple
# print(fruit.items())

# Convert the dictionary into a tuple using tuple() constructor
myTuple = tuple(fruit.items())
print(myTuple)

# Use dict() constructor
# Use a tuple to create a dictionary
print(dict(myTuple))