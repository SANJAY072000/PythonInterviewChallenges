number = int(input("\n Enter a number : "))
i, y = 2, 0
for i in list(range(2, number)):
    if number % i == 0:
         y = 1
         break
if y != 1:
    print("%d is a prime number" %(number))
else:
    print("%d is not a prime number" %(number))




