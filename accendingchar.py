# # accending to decending with usin swapping method
a=['b','a','d','c','l','h']
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

# a=[1,3,2,5,4,6,7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)