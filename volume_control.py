for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
    elif x<y:
        print(y-x)
    else:
        print(x-y)