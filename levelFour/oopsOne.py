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

ph = Phone()
# ph.name = "s79"
# ph.BootLogo()
print(ph.cv)
print(ph.get_cv())
ph.set_cv("Sumit", "Bisht")
print(ph.cv)
print(ph.get_cv())
