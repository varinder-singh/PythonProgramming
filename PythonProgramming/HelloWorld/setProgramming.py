# Set can be created in two ways:

# mySet = {1, 2, 3, 4, 5}
#
# mySet1 = set([1, 3, 5, 7])
#
# print(mySet)
# print(mySet1)
#
# # Set can be created from a list, tuple.
#
# myTuple = (2, 4, 6, 8)
# print(myTuple)
#
# mySet2 = set(myTuple)
#
# print(mySet2)

# Order is not guranteed in a set
# Union operation on a set
# Sets post python 3.6 preserver the ordering ... confirmed by Jean Paul

even = set(range(0, 40, 2))
#print("Length of a set even before union is {}".format(len(even)))
square_tuple = (4, 9, 16, 25, 36)
square = set(square_tuple)
#print("length of a set square formed from a tuple is {}".format(len(square)))

# uni = even.union(square)
#
# print("Length of union is {}".format(len(uni)))
# print(uni)

# Intersection on sets
# We can also do '-' minus of the sets
# print(even.intersection(square))

# Symmetic Difference

# print(even.symmetric_difference(square))
#
# print("=" * 40)
#
# print(square.symmetric_difference(even))


#### Differnce between discard and remove method

# square.discard(8)
#
# square.remove(8) # Gives error if the element is not in set