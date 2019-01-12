# import random module shipped with python

# import random
#
# highest = 10
# answer = random.randint(0,highest)
#
# guess = int(input("Please enter a number between 0 and {0} : ".format(highest)))
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess a higher number")
#     else:
#         print("Pleas guess a lower number")
#     guess=int(input())
#     if guess == answer:
#         print("Well done!, you guessed it right")
#     else:
#         print("Better luck next time!")
# else:
#     print("You got it first time")


# Test 1
value = 8
answer = 0

for x in range(1, 13):
    answer = value * x
    print("{0} times {1} is {2}".format(x, value, answer))