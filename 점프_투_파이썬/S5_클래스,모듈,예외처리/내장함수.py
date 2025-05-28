# enumerate
for i,name in enumerate(['body','foo','bar']):
  print(i,name)

# eval
eval('1+2') # 3
eval ("'hi'+'a'") # 'hia'

# filter
def positive(l):
  result=[]
  for i in l:
    if i>0:
      result.append(i)
  return result

print(positive([1,-3,2,0,-5,6]))

def positive(x):
  return x>0

print(list(filter(positive,[1,-3,2,0,-5,6])))

list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))

# isinstance
class Person:pass

a=Person()
isinstance(a,Person)

# map
def two_times(numberList):
  result=[]
  if number in numberList:
    result.append(number*2)
  return result

result=two_times([1,2,3,4])
print(result)

def two_times(x):return x*2

list(map(two_times,[1,2,3,4]))

list(map(lambda x:x*2,[1,2,3,4]))

# zip
list(zip([1,2,3],[4,5,6])) # [(1,4), (2,5), (3,6)]