# for loop
# can change end separator by providing it into the print function

# for i in range(1,20): # 20 is never included in the range so the program would work from 1 to 19
#     print("i is {} ".format(i))

# Test1
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char,end='')

# Test 2

for i in range(0,101,7):
    print(i)