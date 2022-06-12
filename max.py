a={"nidhi":[20,40,30],"abhishek":[95,100,80],"jyoti":[80,70,90]}
def max_sub(a,i):
	sum=0
	num=val[i]
	for value in a.values():
		if num<=value[i]:
			num=value[i]
	return num
for val in a.values():
	l=len(val)
	for index in range(l):
		print(max_sub(a,index))
	break