# # How about a list holds a tuple.
#
# myList = [1, 2, ("Varinder", 28)]
#
# print(myList)
#
# myList.append(4)
#
# print(myList)
#
# myList[1] = 7
#
# print(myList)
#
# myList[2] = ("Sandhu", 7)
#
# print(myList)
#
# myList[2][1] = 97
#
# print(myList)

# Test 2

trees = ["Larch", "Larch"]
identified_trees = trees

trees.append("Horse Chestnut")
print(identified_trees)


# Test 3

imelda = 'More Mayhem', 'Imelda May', 2011, [
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')]

imelda[3].append((5, 'All For You'))
print(imelda[3])