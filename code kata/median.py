q=int(input())
a=list(map(int,input().strip().split()))[:q]
a.sort()
s=(a[int(len(a)/2)])
print(s)
