my_strimg =(input("enter a string :"))
count={}
for letter in my_strimg:
    if letter in count:
        count[letter]+=1
else:
    count[letter]=1

print("count frequency is..") 
for key,vaule in count.items():
  print(f"{key} occurs {vaule} times")
      


