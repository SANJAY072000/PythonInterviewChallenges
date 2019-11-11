from calcfun import *


def mnu():
    print("\n 1. Add\n 2. Subtract\n 3. Multiply")
    ch = int(input("\n Enter your choice : "))
    if ch == 1:
        print(add())
    elif ch == 2:
        print(sub())
    elif ch == 3:
        print(mul())
    else:
        print("\n Wrong choice")









