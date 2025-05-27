# 계산기
# result=0

# def add(num):
#   global result
#   result+=num
#   return result

# print(add(3))
# print(add(4))

# ---------------------------------------------
# 계산기 2대
# result1=0
# result2=0

# def add1(num):
#   global result1
#   result1+=num
#   return result1

# def add2(num):
#   global result2
#   result2+=num
#   return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(5))

# ------------------------------------------------
class Calculator:
  def __init__(self):
    self.result=0

  def add(self,num):
    self.result+=num
    return self.result
  
  def sub(self,num):
    self.result-=num
    return self.result
  
cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))

# ----------------------------------------------
# 사칙연산 클래스
class FourCal:
  def __init__(self,first,second):
    self.first=first
    self.second=second
  def setdata(self,first,second):
    self.first=first
    self.second=second
  def add(self):
    result=self.first+self.second
    return result
  def sub(self):
    result=self.first-self.second
    return result
  def mul(self):
    result=self.first*self.second
    return result
  def div(self):
    result=self.first/self.second
    return result
  

a=FourCal()
a.setdata(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

# MoreFourCal 클래스
class MoreFourCal(FourCal):
  def pow(self):
    result=self.first**self.second
    return result
  
# SafeFourCal 클래스
class SafeFourCal(FourCal):
  def div(self):
    if self.second==0:
      return 0
    else:
      return self.first/self.second