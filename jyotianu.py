dic = [{'name':'anurag'},{'name':'ritika'},{'name':'anuradha'}]
l=[]
for i in dic:
    l.append(i['name'][0])
# print(l)
count=0
l1=[]
for j in l:
    # print(j)
    if j not in l1:
        l1.append(j)
        count=l.count(j)
        print(j,count)


