ans=[]
n=int(input())
l=list(map(int, input().split()))
ans.append(l[0])
curmax=0
for i in range(1, len(l)):
    if l[i]>curmax:
        curmax=l[i]
        ans.append(l[i])

for j in ans:
    print (j, end=' ')