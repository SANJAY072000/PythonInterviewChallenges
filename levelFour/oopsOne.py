class Phone:
    name = "S10"
    brand = "Samsung"
    cv = "Sanjay"
    def get_cv(self):
        return self.cv
    def set_cv(self, nn, sn):
        self.cv = nn + sn
    def BootLogo(self):
        print(self.name, "Samsung")

class Samsung:
    def __init__(self):
        print("I am Samsung")

    def makeScreen(self):
        print("I make screens")

    def test(self):
        print("Screen Tests 1")
        print("Screen Tests 2")
        print("Screen Tests 3")

# ph = Phone()
# # ph.name = "s79"
# # ph.BootLogo()
# print(ph.cv)
# print(ph.get_cv())
# ph.set_cv("Sumit", "Bisht")
# print(ph.cv)
# print(ph.get_cv())
