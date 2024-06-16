n=int(input())
l=list(map(int, input().split()))

def findmin(l):
    minval=l[0]
    minindex=0
    for i in range(1,len(l)):
        if l[i]<minval:
            minval=l[i]
            minindex=i
        elif l[i]==minval:
            minindex=i
    return minval, minindex

def findmax (l):
    maxval=l[0]
    maxindex=0
    for i in range(1, len(l)):    
        if l[i]>minval:
            maxval=l[i]
            maxindex=i
    return maxval, maxindex

def snt(a):
    if a<=3:
        return a>1
    if a%2==0 or a%3==0:
        return False
    i=5
    while i<=a**0.5:
        if a%i==0 or a%(i+2)==0:
            return False
        i+=6
    return True

def capmax(l):
    max1 = max2= float('-inf')
    min1 = min2= float('inf')
    for i in l:
        if i>max1:
            max2=max1
            max1=i
        elif i>max2:
            max2=i
    
        if i<min1:
            min2=min1
            min1=i
        elif i<min2:
            min2=i
            
    ansmax = max1 * max2
    ansmin = min1 * min2
    
    return max(ansmax,ansmin)

def doixung (l):
    return l==l[::-1]


a=0
dem=1
minval,minindex=findmin(l)
maxval,maxindex=findmax(l)
print (maxval,maxindex)
print (minval,minindex)
for i in l:
    if snt(i):
        a+=1
print(a)
print(capmax(l))
if doixung(l):
    print('YES')
else:
    print('NO')
for j in l:
    dem*=j
print(dem)