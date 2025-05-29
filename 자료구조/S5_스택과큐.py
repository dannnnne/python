class Stack:
  def __init__(self):
    self.container=list()
    # 내부 표현 : 실제로 데이터를 담을 객체는 동적 배열

  def empty(self):
    if not self.container:
      return True
    else:
      return False
    
  def push(self,data):
    self.container.append(data)

  def pop(self):
    if self.empty():
      return None
    return self.container.pop()
  
  def peek(self):
    if self.empty():
      return None
    return self.container[-1]
  
s=Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

while not s.empty():
  print(s.pop(), end='')

#------------------------------------

#  Queue 
class Queue:
  def __init__(self):
    self.container=list()

  def empty(self):
    if not self.container:
      return True
    else:
      return False
    
  def enqueue(self,data):
    self.container.append(data)

  def dequeue(self,data):
    return self.container.pop(0)

  def peek(self):
    return self.container[0]
  
class CQueue:
  MAXSIZE=10
  def __init__(self):
    self.container=[None for _ in range(CQueue.MAXSIZE)]
    self.front=0
    self.rear=0

  def is_empty(self):
    if self.front==self.rear:
      return True
    else:
      return False
    
  def __step_forward(self,x):
    # 편의 함수 : front나 rear를 뒤로 이동했을 때 동적 배열을 벗어난다면 동적 배열의 맨 처음으로 이동시킨다.
    x+=1
    if x>=CQueue.MAXSIZE:
      x=0
    return x
  
  def is_full(self):
    next=self.__step_forward(self.rear)
    if next==self.front:
      return True
    return False
  
  def enqueue(self,data):
    if self.is_full():
      raise Exception("The queue is full")
    self.container[self.rear]=data
    self.rear=self.__step_forward(self.rear)

  def dequeue(self):
    if self.is_empty():
      raise Exception("The queue is empty")
    ret=self.container[self.front]
    self.front=self.__step_forward(self.front)
    return ret
  
  def peek(self):
    if self.is_empty():
      raise Exception("The queue is empty")
    return self.container[self.front]

# ------------------------------

# deque
from collections import deque

print('*'*20+'STACK'+'*'*20)
stack=deque()
for i in range(1,6):
  stack.append(i)
  print(stack)
for i in range(5):
  print(stack.pop())

print('*'*20+'STACK'+'*'*20)

queue=deque()
for i in range(1,6):
  queue.append(i)
  print(queue)
for i in range(5):
  print(queue.popleft())