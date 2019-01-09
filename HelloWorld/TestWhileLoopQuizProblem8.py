# Test 8
choice = 'None'

while(choice != '0'):
    choice = input("Please enter your choice.  Press enter to quit ")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")