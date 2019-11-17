class Phone:
    name = "S10"
    brand = "Samsung"
    def BootLogo(self):
        print(self.name, "Samsung")
    def __init__(self, a):
        self.name = a

ph = Phone("S35")
ph.name = "s79"
ph.BootLogo()


