# Write a program to append the sample.txt with times table.
# The first column of the table should be right justified.

# Example is -
# 1 times 2 is 2
# 2 times 2 is 4
#
#
#

with open('sample1.txt', 'a') as sampleText:
    for i in range(0, 10):
        print("{0:>2} times {2:>4} is {2:>6}".format(2, i, 2*i), file=sampleText)