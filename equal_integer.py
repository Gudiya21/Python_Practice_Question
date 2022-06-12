def name(x,y):
    if x==y:
        return 0
    elif x<y:
        return y-x
    
    elif (x-y)%2==0:
        return (x-y)//2
    elif (x-y)%2!=0:
        return (x-y)//2 +2
    
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    print(name(x,y))
        