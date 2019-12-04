from requests import *
from bs4 import *

r = get("http://innoskrit.in/")
s = BeautifulSoup(r.text, 'lxml')
print(len(s.select("p")))


