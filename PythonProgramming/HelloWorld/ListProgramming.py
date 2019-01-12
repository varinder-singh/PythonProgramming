# This program understands to make a list and how to iterate the list via for loop
# Use of append operation over list.
# USe of sort operation over the list. Sort on the list in python never creates a new object it does the operation on
# the same object.
#

groceryList = ['bread', 'butter', 'rice', 'lentils', 'jam', 'cup cakes', 'dosa batter']
# groceryList.append("sambar masala")
# groceryList.sort()
#
# # However, if we try to print the above statement it returns NONE.
# print(groceryList.sort())
# # If at all a new list object is needed then use the method 'sorted()'
# print(sorted(groceryList))
# Two lists can be concatenated using '+' operator in python
print()

x = 1


print("******************Start of Grocery List**********************")
for item in groceryList:
    print("Item # {0} is {1}".format(x,item))
    x+=1
print("******************End of Grocery List************************")