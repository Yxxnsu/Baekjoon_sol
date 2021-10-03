import math

a,b,c = map(int , input().split())
if(c - b <= 0):
    print(-1)
else: print(math.floor(a / (c-b) + 1))



a,b,c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)