# # Use join() to concatenate the single string as general concatenation results in a new string always.
#
# value = "a", "b", "c", "d"
#
# result = ','.join(value)
#
# print(result)

exists = [{"Q": {0: "You are sitting in front of  a computer"}}, {"W": 2, "E": 3, "N": 5, "S": 4, "Q": {0: "You are sitting in front of  a computer"}},
          {"N": 5, "Q": {0: "You are sitting in front of  a computer"}}, {"W": 2, "Q": {0: "You are sitting in front of  a computer"}}, {"N": 5, "W": 2, "Q": {0: "You are sitting in front of  a computer"}},
          {"W": 2, "S": 1, "Q": {0: "You are sitting in front of  a computer"}}]

loc = 1

while True:
    availableExits = ','.join(exists[loc].keys())

    if loc == 0:
        break

    direction = input("Available exits are : {} : ".format(availableExits)).upper()
    print()
    if direction in availableExits:
        loc = exists[loc].get(direction)
    else:
        print("You cannot go in this direction")