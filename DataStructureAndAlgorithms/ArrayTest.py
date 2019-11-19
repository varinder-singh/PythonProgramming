N = int(input())

# Get the array
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic:
for i in range(N):
    sumArray[i] = numArray1[i] + numArray2[i]


# Print the sumArray
for element in sumArray:
    print(element, end=" ")

print("")