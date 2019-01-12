# join() method for string concatenation as generally concatenating a string produces a new string always.
# split() method for string splitting. Split happens on the specified delimiter.
# Challenge Dictionary using join operation.

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of the road before a small brick building",
             2: "You are at the top of the hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are is a valley beside a stream",
             5: "You are in a forest"
             }

exits = {"Q": 0,
         "S": 1,
         "E": 2,
         "N": 3,
         "W": 4
         }
while True:
    availableExits = ','.join(exits.keys())
    direction = input("Please enter your new direction out of {} ".format(availableExits)).upper()
    if direction == "Q":
        break
    elif direction in exits.keys():
        value = exits.get(direction)
        print(locations.get(value))
    else:
        print("There is no such direction present")
print("Exited the game")