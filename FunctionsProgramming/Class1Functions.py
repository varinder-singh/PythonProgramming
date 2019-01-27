# if in the function call we give a named parameter it is optional to pass the parameter when the function is passed


def multiply():
    print("Multiply: Result without parameters : {}".format(4*4))


def sum(a, b=0):
    print("Sum: Result with parameters : {}".format(a + b))


multiply()
sum(4)