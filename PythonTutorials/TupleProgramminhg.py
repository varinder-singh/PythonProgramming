# # Tuples can be easily unpacked into variables
#
# myTuple = "Varinder", "CSE", 28
# print(myTuple)
# name, course, age = myTuple
#
# print(name)
# print(course)
# print(age)

# Test 1
imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Haltz"))

artist, album, year, tracks =imelda
track1, track2, track3, track4 = tracks

print(artist)
print(album)
print(year)
print(track1[0], track1[1])
print(track2[0], track2[1])
print(track3[0], track3[1])
print(track4[0], track4[1])