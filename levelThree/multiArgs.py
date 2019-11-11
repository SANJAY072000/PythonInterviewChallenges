def add(*n):
    s = 100
    for i in n:
        s -= i
    return s


p1 = int(input())
p2 = int(input())
print(add(p1, p2))



