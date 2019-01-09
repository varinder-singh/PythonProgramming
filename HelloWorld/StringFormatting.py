# Various ways to format strings in python
# Replacement String format method.
# Format method is depricated in python 3

age = 28
name = "Varinder"
print("""My name is {1} 
and my age is {0} years""".format(age,name))

# Use %d - integers %s - strings, %f - float, again deprecated
print("My age is %d %s and my name is %s"%(age, "years", name))

# Try string formatting in a for loop

for i in range(1,12):
    print("%2d square is %4d and cube is %4d"%(i,i**2,i**3))

# Use of floating Numbers
print("Pi is approximately %16f"%(22/7))

# Use decimal precision
print("Pi's is approximately %12.50f"%(22/7))


# Use replacement method {} in the formatting like above
# Use of number inside the {} is optional as python does the replacement based on the occurrence of values inside the
# .format() method
for i in range(1,12):
   print("{0:2} square is {1:4} and cube is {2:4}".format(i,i**2,i**3))

print("Pi is approximately {0:12.50f}".format(22/7))