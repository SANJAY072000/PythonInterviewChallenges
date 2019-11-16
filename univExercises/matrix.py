# m = [[1, 2, 3], [4, 5, 6]]
r = int(input("\n Enter rows : "))
c = int(input("\n Enter columns : "))
m = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    m.append(a)
for i in range(r):
    for j in range(c):
        print(m[i][j], end=' ')
    print()



