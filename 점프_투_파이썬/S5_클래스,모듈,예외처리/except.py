# try, finally
f=open('foo.txt','w')
try:
  # 무언가를 수행한다.
finally:
  f.close()

# 여러 개의 오류 처리하기
try:
  a=[1,2]
  print(a[3])
  4/0
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")
except IndexError:
  print("인덱싱할 수 없습니다.")

# 2개 이상의 오류 동시에 처리하기
try:
  a=[1,2]
  print(a[3])
  4/0
except (ZeroDivisionError,IndexError) as e:
  print(e)

# 오류 회피하기
try:
  f=open('나없는파일','r')
except FileNotFoundError:
  pass

# 오류 일부러 발생시키기
class Bird:
  def fly(self):
    raise NotImplementedError
  
class Eagle(Bird):
  pass

eagle=Eagle()
eagle.fly()

class Eagle(Bird):
  def fly(self):
    print("very fast")

# 예외 만들기
class MyError(Exception):
  def __str__(self):
    return "허용되지 않는 별명입니다."

def say_nick(nick):
  if nick=="바보":
    raise MyError()
  print(nick)

say_nick("천사")
say_nick("바보")

try:
  say_nick("천사")
  say_nick("바보")
except MyError :
  print("허용되지 않은 별명입니다.")

try:
  say_nick("천사")
  say_nick("바보")
except MyError as e:
  print(e)