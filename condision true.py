def test(x,y):
 if x==y or abs(x-y)==5 or x+y==5:
  return True
 else:
  return False
  
print(test(2,3))
print(test(15,10))
print(test(66,88))