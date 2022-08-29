l=[2,5,1,7,3,9]
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
        j+=1
    i+=1
print("sorted list:",l)
if len(l)%2==0:
	ele=len(l)//2
	print("medium is:",l[ele-1],l[ele])
else:
	ele=(len(l)-1)//2
	print("medium is:",l[ele])



