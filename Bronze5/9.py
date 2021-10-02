a = [1, 1, 2, 2, 2, 8]
L = list(map(int, input().split()))

for i in range(len(a)):
    print(a[i] - L[i], end=" ")
