
fruit = {"apple": "good for cider",
         "orange": "sweet citrus fruit",
         "lemon": "citrus fruit",
         "banana": "full of potassium"}

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmmm, lovely",
       "lemon": "citrus fruit but a vegetable",
       "spinach": "can i have some more vegetables please?"}

print("+" * 40)
print()
print(veg)
print("+" * 40)

# veg.update(fruit) # does not return a new copy of the dictionary rather update the same dictionary object. Updates the existing key-value or add new items in the dictionary
# print(veg)
# print("+" * 40)

# in order to get the copy of updated dictionary in a new object use copy() operation

copyOfFruit = fruit.copy()
print("copy of fruit {}".format(copyOfFruit))
veg.update(copyOfFruit)
print(veg)
print("+" * 40)