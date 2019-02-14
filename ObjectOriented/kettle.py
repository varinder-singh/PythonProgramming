class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price


kenwood = Kettle("Kenwood", 1299)
hamilton = Kettle("Hamilton", 1599)

print("Make is {} and it cost you {}".format(kenwood.make, kenwood.price))
