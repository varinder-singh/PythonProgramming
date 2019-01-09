# input the ip address from the user
ipAdd = input("Please enter the IP Address : ")
y = ""
print("length of ip {0}".format(len(ipAdd)))

for x in ipAdd:
    if x != '.':
        y += x
    elif x == '.':
        print("Length of the Segment is {0} ".format(len(y)))
        y = ""
    else:
        print("I am in loop")

print("Program ends here")