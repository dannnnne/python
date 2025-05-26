def add(a,b):
  return a+b

a=3
b=4
c=add(a,b)
print(c)

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
  result=0
  for i in args:
    result+=i
  return result

result=add_many(1,2,3)
print(result)

# 여러 개의 매개변수를 받는 함수
def add_mul(choice,*args):
  if choice=="add":
    result=0
    for i in args:
      result+=i
  elif choice=="mul":
    result=1
    for i in args:
      result*=i
  return result

result_add=add_mul("add",1,2,3,4)
result_mul=add_mul("mul", 1,2,3,4)
print(result_add)
print(result_mul)

# 키워드 파라미터
def print_kwargs(**kwargs):
  print(kwargs)

print_kwargs(a=1)

# 함수의 결과값은 언제나 하나이다
def add_and_mul(a,b):
  return a+b, a*b

result1,result2=add_and_mul(3,4)
print(result1)
print(result2)

def add_and_mul2(a,b):
  return a+b
  return a*b

result=add_and_mul2(3,4)
print(result)
# 결과 값은 하나만 나온다. return 문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나온다.   

# return의 또 다른 쓰임새
def say_nick(nick):
  if nick=="바보":
    return
  print("나의 별명은 %s입니다."%nick)

say_nick("바보")
say_nick("다은")

# 매개변수에 초기값 미리 설정하기
def say_myself(name,old,man=True):
  print("나의 이름은 %s입니다." %name)
  print("나이는 %d살입니다."%old)
  if man:
    print("남자입니다.")
  else:
    print("여자입니다.")

say_myself('다은',23,False)
# 초기값을 설정해놓은 매개변수 뒤에 초기값을 설정하지 않은 매개변수는 올 수 없다.

# ------------------------------------------------------
# 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과 전혀 상관없다.

# def vartest(a):
#   a=a+1

# vartest(3)
# print(a)
# 오류 발생

# ----------------------------------------------------
# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a=1
def vartest(a):
  a+=1
  return a
a=vartest(a)
print(a)

# 2. global 명령어 사용하기기
b=1
def vartest_global():
  global b
  b+=1

vartest_global()
print(b)

# ----------------------------------
# lambda
add=lambda a,b:a+b
result=add(4,5)
print(result)

# ------------------------------------
#  사용자 입력
# a=input()
a=input()
print(a)

b=input("숫자를 입력하세요.")

# -------------------------------------
# 사용자 출력
# 큰따옴표로 둘러싸인 문자열은 +연산과 동일하다
# 문자열 띄어쓰기는 콤마로 한다.
# 한 줄에 결과값 출력하기 : end='  '