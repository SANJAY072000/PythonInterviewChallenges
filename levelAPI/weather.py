from json import *
from requests import *


a = lambda u: str(loads(get(u).text)["main"]["temp"]) + " F"


print("\n In London, temperature is ", a("https://samples.openweathermap.org/data/2.5/weather?q=London&appid=b6907d289e10d714a6e88b30761fae22"))













