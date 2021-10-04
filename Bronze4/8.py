a,b,c, = sorted(map(int, input().split()))
print(a,b,c)

Ar = list(map(int, input().split()))
Ar.sort()
print(Ar[0], Ar[1], Ar[2])

print(*sorted(map(int,input().split())))