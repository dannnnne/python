# 예제 1. 구구단
def GuGu(dan):
  result=[]
  for i in range(1,10):
    result.append(dan*i)
  return result

result=GuGu(2)
print(result)

# while
# def GuGu(dan):
#   result=[]
#   i=1
#   while i<10:
#     result.append(dan*i)
#     i+=1
#   return result
# ------------------------------------------------------

# 예제 2. 3과 5의 배수 합하기
result=0

for i in range(1000):
  if i%3==0 or i%5==0:
    result+=i

print(result)

# 예제 3. 게시판 페이징하기
def getTotalPage(m,n):
  if m%n==0:
    return m//n
  else:
    return m//n+1
  
print(getTotalPage(5,10))

# 예제 4. 간단한 메모장 만들기
# C:/doit/memo.py
import sys
option=sys.argv[1]
if option=='-a':
  memo=sys.argv[2]
  f=open('memo.txt','a')
  f.write(memo)
  f.write('\n')
  f.close()
elif option=='v':
  f=open('memo.txt')
  memo=f.read()
  f.close()
  print(memo)

# 예제 5. 탭을 4개의 공백으로 바꾸기
import sys

src=sys.argv[1]
dst=sys.argv[2]

f=open(src)
tab_content=f.read()
f.close()

space_content=tab_content.replace("\t"," "*4)

f=open(dst,'w')
f.write(space_content)
f.close()

# 예제 6. 하위 디렉터리 검색하기
import os

def search(dirname):
  try:
    filenames=os.listdir(dirname)
    for filename in filenames:
      full_filename=os.path.join(dirname,filename)
      if os.path.isdir(full_filename):
        search(full_filename)
      else:
        ext=os.path.splitext(full_filename)[-1]
        if exit=='.py':
          print(full_filename)
  except PermissionError:
    pass

search("c:/")