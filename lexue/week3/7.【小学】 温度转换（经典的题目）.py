t = input()
c = t.split()
char = c[0]
x = float(c[1])
if char == "F" :
    y = x * 9 / 5 + 32
    print("The Centigrade is {:.2f}".format(y))
else:
    y = (x - 32) *5 / 9
    print("The Fahrenheit is {:.2f}".format(y))