# 18-30 holiday package
fName = input("Please enter your first name :")
lName = input("Thank you!, Now please enter your last name :")

age = int(input("Please enter your age :"))

if 18<= age <=30:
    print("Welcome! {},{}  on board where are you planning to go this year".format(lName,fName))
else:
    print("{},{} We apologize but we cannot plan a trip for you".format(lName,fName))