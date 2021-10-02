a, b = map(int, input().split())
L = map(int, input().split())

for i in L:
    print(i - a * b)


L, P = map(int, input().split())
news = list(map(int, input().split()))
N = L * P
for i in range(len(news)):
    news[i] -= N
for new in news:
    print(new, end=" ")
