def yanghui(n) :
    #杨辉三角
    l = [1]
    while True:
       yield l
       l.append(0)
       l = [l[i-1] + l[i] for i in range(len(l))]

n = 0
for t in yanghui(10):
    print(t)
    n = n + 1
    if n >= 10:
        break
