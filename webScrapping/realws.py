from requests import *
from bs4 import *

r = get("https://en.wikipedia.org/wiki/Machine_learning")
s = BeautifulSoup(r.text, 'lxml')
for i in s.select(".toctext"):
    print(i.text)




