y , m , d = map(int , input().split())
cnt = 0
mon = (0,31,28,31,30,31,30,31,31,30,31,30,31)
i = 1900
while i < y:
    cnt = cnt + 365
    if (i%4 == 0 and i%100!=0) or i%400 == 0:
        cnt = cnt + 1
    i= i + 1
i = 1
while i < m:
    cnt = cnt + mon[i]
    if i == 2:
        if (y%4 == 0 and y%100!=0) or y%400 == 0:
            cnt = cnt + 1
    i = i + 1
cnt = cnt + d
week = cnt % 7
print(f"{week}")
