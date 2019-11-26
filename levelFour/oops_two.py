from oopsOne import *

class Iphone(Samsung):
    def __init__(self):
        super().__init__()

    def a3chips(self):
        print("I make a3chips")

    def itest(self):
        print("Iphone tests")
        self.test()
    # def makeScreen(self):
    #     print("Iphone makes screens")
    #     super().makeScreen()

iph = Iphone()
# iph.a3chips()
# iph.makeScreen()
# iph.itest()