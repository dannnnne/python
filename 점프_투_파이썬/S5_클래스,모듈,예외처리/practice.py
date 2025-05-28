# 1
class Calculator:
  def __init__(self):
    self.value=0

  def add(self,val):
    self.value+=val

class UpgradeCalculator(Calculator):
  def minus(self,val):
    self.value-=val

# 2
class MaxLimitCalculator(Calculator):
  def add(self,val):
    self.value+=val
    if self.value>=100:
      self.value=100

# 4
list(filter(lambda x:x>0,[1,-2,3,-5,8,-3]))

# 6
list(map(lambda x: x*3,[1,2,3,4]))