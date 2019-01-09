# Very Important to understand the difference between a list created using assignment vs using constructor
#
# list_1 = ['1', '2', '3', '4']
# list_2 = list(['1', '2', '3', '4'])
# list_3 = list("Hello World!")
# list_4 = list('1', '2')
#
#
# print("List {}- {}".format("1", list_1))
# print("List {}- {}".format("2", list_2))
# print("List {}- {}".format("3", list_3))

# Difference between '==' and 'is' operator when comparing lists
# '==' compares the content of the list whereas is compares the references
# list_1 = ['1', '2', '3', '4']
# list_2 = list(list_1)
#
# if list_1 is list_2:
#     print("Yes! the lists are equal")
# else:
#     print("No! they are not")

# Test 1

menu = []
menu.append(['eggs', 'sausage', 'bacon'])
menu.append(['eggs', 'spam', 'sausage', 'bacon'])
menu.append(['eggs', 'sausage', 'bacon', 'spam'])
menu.append(['eggs', 'spam', 'sausage', 'spam', 'bacon'])
menu.append(['eggs', 'spam', 'spam', 'sausage', 'bacon'])
menu.append(['eggs', 'sausage', 'spam', 'bacon', 'spam'])

for meal in menu:
    if 'spam' not in meal:
        print(meal)
        for item in meal:
            print(item)