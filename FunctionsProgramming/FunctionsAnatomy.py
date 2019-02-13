# how to create function that accepts multiple parameters
# list comprehension is the efficient way to concatenate string which Tim will disuss in section-14
# go learn the join() gain

# noinspection PyInterpreter
def center_text(*args):
    # noinspection PyInterpreter
    for arg in args:
        left_margin = (80 - len(arg)) // 2
        print(" " * left_margin, arg)


center_text("hello", "hellooooo", "hellooooooooo")