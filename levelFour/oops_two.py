class Samsung:
    def __init__(self):
        print("I am Samsung")

    def makeScreen(self):
        print("I make screens")

    def test(self):
        print("Screen Tests 1")
        print("Screen Tests 2")
        print("Screen Tests 3")

class Iphone(Samsung):
    def __init__(self):
        print("I am IPhone")

    def a3chips(self):
        print("I make a3chips")

    def itest(self):
        print("Iphone tests")
        self.test()

iph = Iphone()
# iph.a3chips()
# iph.makeScreen()
iph.itest()