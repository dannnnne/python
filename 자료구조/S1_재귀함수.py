# factorial 함수
def factorial(n):
  if n<=0:
    return 1
  return factorial(n-1)*n

if __name__=="__main__":
  for i in range(1,6):
    print(factorial(i))

# 스택 프레임
def add_two(a,b):
  c=a+b
  return c

a=10
b=20
result=add_two(a,b)
print(result)

# permutation
def permutation(arr,start):
  if len(arr)-1==start:
    print(arr)
    return
  
  for idx in range(start,len(arr)):
    arr[start], arr[idx]=arr[idx],arr[start]
    permutation(arr,start+1)
    arr[start],arr[idx]=arr[idx],arr[start]

if __name__=="__main__":
  arr=[1,2,3]
  permutation(arr,0)