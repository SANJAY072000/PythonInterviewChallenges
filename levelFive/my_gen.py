from random import *
heros = ["bat", "hulk", "thor"]
for i in heros:
    print(i, end=' ')
print()

def magic():
    for i in range(6):
        yield randint(1, 20)
print(list(magic()))

# for i in list(magic()):
#     print(i)



