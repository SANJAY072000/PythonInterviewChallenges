l = int(input("\n Enter lower range :"))
u = int(input("\n Enter upper range :"))

for i in list(range(l, u + 1)):
    y = 0
    for j in list(range(2, i)):
        if i % j == 0:
            y = 1
            break
    if y != 1:
        print(i, end=' ')




