na=input("enter line 0f string :")
n=na.split()
longest=len(n[0:])
for i in n:
 if len(i)>longest:
  longest=len(i)
print("longest string length =",longest)