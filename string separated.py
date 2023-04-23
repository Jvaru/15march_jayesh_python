a2,a1='abcd','rstu'
temp=a2
a2=a1[0:2]+a2[2:]
a1=temp[0:2]+a1[2:1]
print(a2+''+a1)