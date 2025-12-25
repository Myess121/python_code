# t = input()
# s = t.split()
# a1 = int(s[0])
# a2 = int(s[1])
#等价于：
a1,a2 = map(int , input().split())

if a1 > a2:
    print(a1 , ">" , a2)
elif a1 < a2:
    print(f"{a1} < {a2}")
else :
    print("两数相等，都为{}".format(a1))