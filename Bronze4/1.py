import math

a, h, w = map(int, input().split())

r = a / math.sqrt(math.pow(h, 2) + math.pow(w, 2))
print(math.floor(r * h), math.floor(r * w))
