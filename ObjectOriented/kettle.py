class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 1299)
hamilton = Kettle("Hamilton", 1599)

print("Make is {} and it cost you {}".format(kenwood.make, kenwood.price))

print("Make is {0.make} and it cost you {0.price}".format(hamilton))