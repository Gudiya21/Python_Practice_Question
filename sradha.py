x=int(input("enter "))
c=0
for i in range(1,x+1):
  if x%i==0:
    c+=1
if c==2:
  print("prime no.")
else:
  print("composite no.")