year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 4 == 0 and year % 400 == 0:
    print(1)
else: print(0)

n=int(input())
if n%4==0 and n%100!=0 or n%400==0:
    print(1)
else:
    print(0)