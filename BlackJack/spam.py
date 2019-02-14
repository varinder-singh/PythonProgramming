def spam1():

    def spam2():

        def spam3():
            z = "spam"
            print("Locals in spam3() : {}".format(locals()))
            return z

        y = "more " + x
        y += spam3()
        print("Locals in spam2() : {}".format(locals()))
        return y

    x = "even "
    x += spam2()
    print("Locals in spam1() : {}".format(locals()))
    return x


print("Final Outcome -------------> {}".format(spam1()))
