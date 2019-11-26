from oopsOne import *

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