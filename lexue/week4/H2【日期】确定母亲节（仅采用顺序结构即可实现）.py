n = int(input())
a = 4
while n > 2014 :
    a = a + 1
    if (n%4 == 0 and n%100 != 0) or n%400 == 0:
        a = a + 1
    n = n - 1
while a >= 7:
    a = a - 7
if a == 0:
    print("8")
else:
    print("{}".format(15-a))
