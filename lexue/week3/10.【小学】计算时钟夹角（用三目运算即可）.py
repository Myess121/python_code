a,b = map(float, input().split())
c = a * 30 - b * 6 + b * 0.5
if c < 0:
    c = c + 360

if c >= 180:
    c = 360 - c
print(f"{c:.1f}")
