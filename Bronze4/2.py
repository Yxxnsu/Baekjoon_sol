a, b = map(int, input().split())
print('>' if a > b else ('<' if a < b else '=='))

a, b = [int(x) for x in input().split()]
print('>' if a > b else ('<' if a < b else '=='))