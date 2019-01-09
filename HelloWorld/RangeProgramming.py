# List can be created with the range function

myList = list(range(10))
print(myList)

# Test range with slices

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)

print("*" *50)
for i in o:
    print(i, end=',')
print()
print("*" *50)
for i in p:
    print(i, end=',')