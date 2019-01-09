# Question asked in QnA section why numbers are always sorted in set whereas strings are not

name1 = "Gijs Van Den"
name2 = "J-P Roberts"

for x in range(6):
    print(hash(x)) # Hashing an int returns an int

print(hash(name1)) # a long integer is returned
print(hash(name2))