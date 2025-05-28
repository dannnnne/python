# pickle
import pickle
f=open("test.txt",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close()

import pickle
f=open("test.txt",'rb')
data=pickle.load(f)
print(data)

# OS
import os
os.environ

# shutil
import shutil
shutil.copy("src.txt","dst.txt")

# glob
import glob
glob.glob("c:/doit/mark/*")

# tempfile
import tempfile
filename=tempfile.mkstemp()

import tempfile
f=tempfile.TemporaryFile()
f.close()

# time.sleep
import time
for i in range(10):
  print(i)
  time.sleep(1)

# random
import random
def random_pop(data):
  number=random.randint(0,len(data)-1)
  return data.pop(number)

if __name__=="__main__":
  data=[1,2,3,4,5]
  while data: print(random_pop(data))

def random_pop(data):
  number=random.choice(data)
  data.remove(number)
  return number