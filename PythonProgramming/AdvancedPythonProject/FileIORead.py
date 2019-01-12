# Use open and close methods to read the content of the file .
# open function takes 2nd optional argument to opne the file in a specific mode
# close ensures the integrity of the file after the operations on the file ends

# jabber = open('sample.txt','r')
#
# for line in jabber:
#     print(line)
#
# jabber.close()

# Python 2.5 and later have 'WITH' keyword which manages the unmanaged resources.
# there is no need to use close() as 'WITH' handles everything even if the exception occurs it closes the file.

# with open('sample.txt','r') as jabber:
#     for line in jabber:
#         print(line)
# print("="*70)
# with open('sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
#     print(lines)
#     print("total number of lines {}".format(len(lines)))
# print("="*70)
# for line in lines[::-1]:
#        print(line, end='')

##################### read() is generally used for reading binary data

with open('sample.txt', 'r') as jabber:
    lines = jabber.read()
print("="*70)
for line in lines[::]:
    print(line, end='')