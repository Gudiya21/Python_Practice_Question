# for cas in range(int(input())):
#     n = input()
#     a = [0] + map(int,input().strip().split())
#     b = map(int,input().strip().split())
#     print(sum(b[i] <= a[i+1] - a[i] for i in range(n)))

# cook your dish here
# for _ in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     res=0
#     for i in range(n):
#         if i==0 and a[i]>=b[i]:
#             res+=1
#         elif (a[i]-a[i-1])>=b[i]:
#             res+=1
#     print(res)



n=int(input("enter n value"))

while(n>0):
    x=int(input("enter x value"))
    a=list(map(int,input().split('enter a value ')))
    b=list(map(int,input().split('enter b value ')))
    count=0
    for i in range(x):
        if i==0:
            if b[0]<=a[0]:
                count+=1
        else:
            diff=a[i]-a[i-1]
            if diff>=b[i]:
                count+=1
    print("output is",count)
    n-=1