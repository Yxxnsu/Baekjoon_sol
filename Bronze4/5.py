a, b, c = map(int, input().split())
 
if a == b == c:
    print(10000 + a * 1000)
elif a == b or b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + a * 100)
else:
    print(max(a, b, c)*100)


a=list(map(int,input().split()))
b=sorted(set(a),key=a.count)
print([10000+b[-1]*1000,1000+b[-1]*100,max(b)*100][len(b)-1])

s = list(map(int, input().split()))
if len(set(s))==1 : print(max(s)*1000+10000)
elif len(set(s))==2 : print(sorted(s)[1]*100+1000)
else : print(max(s)*100)

# sorted
a,b,c=sorted(map(int,input().split()))
print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)