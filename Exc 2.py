n=int(input())
l=list(map(int,input().split()))

def sosanh (l):
    for i in range(len(l)-1):
        if l[i] >= l[i + 1]:
            return False
    return True
        
if sosanh(l):
    print('YES')
else:
    print('NO')