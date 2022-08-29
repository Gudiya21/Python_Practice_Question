# WITH USING SWAPING

a=[2,5,1,0,3,9]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)


# WITHOUT USING SWAPING

a=[2,5,1,0,3,9]
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
        j+=1
    i+=1
print(a)