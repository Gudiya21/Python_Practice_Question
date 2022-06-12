a={"nidhi":[20,25,30],"abhishek":[95,100,80]}
count=0
for key in a:
	count+=1
def sum_sub(a,i):
	sum=0
	for value in a.values():
		sum+=value[i]
	return sum
for val in a.values():
	l=len(val)
	for index in range(l):
		print(sum_sub(a,index))
		#print(sum_sub(a,index)/count)
	break