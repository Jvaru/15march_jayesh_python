string=input("write string ")
str=str.split(string) 
i=0
counte=0
while i<len(str):
 counte=0
 for j in str:
  if str[i]==j:
   counte=counte+1
  print(str [i],"present",counte ,"times")
 
 i=i+1

  