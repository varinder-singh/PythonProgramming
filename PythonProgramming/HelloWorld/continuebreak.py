# create a list to iterate over using for loop
# Remember : List iterate is not sequential in python

# shopping_list = {"bread", "butter", "jam", "garlic bread", "spam", "peanut butter"}
#
# print("************************ Continue For Loop ********************************")
# for item in shopping_list:
#     if item == "spam":
#         print("caught you!")
#         continue
#     print("Buy : "+item)
#
# print("************************ Break For Loop ********************************")
# for item in shopping_list:
#     if item == 'spam':
#         print("caught you!")
#         break
#     print("Buy : " + item)

#Test 1
print("**************************** Printing result for Test 1 *************************")
for i in range(0, 100, 7):
    if i != 0 and i % 11 == 0:
        print(i)
        break
    else:
        print(i, end = ' ')
        continue

# Test 2
print("**************************** Printing result for Test 2 *************************")
for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i, end = ' ')