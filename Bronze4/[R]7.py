h,m,s = map(int, input().split())
cook = int(input())

s += cook % 60
if s > 59:
    s -= 60
    m += 1
cook = cook // 60

m += cook % 60
if m > 59:
    m -= 60
    h += 1
cook = cook // 60

h += cook % 24
if h > 23:
    h -= 24

print(h,m,s)