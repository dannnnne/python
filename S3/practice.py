a="Life is too short, you need python"

if "wife" in a:print("wife")
elif "python" in a and "you" not in a:print("python")
elif"shirt" not in a:print("shirt")
elif "need" in a:print("need")
else:print("none")

# 예상 답 : shirt
# 실제 답 : shirt

num=0
sum=0

while num<1000:
  num+=1
  if num%3==0:
    sum+=num
  else:continue

print(sum)

# -----------------

i=1

while i<=5:
  print("*"*i)
  print(" ")
  i+=1

# -----------------
for i in range(1,101):
  sum+=i

print(sum)

# -----------------
score=[70,60,55,75,95,90,80,80,85,100]
average=0
sum=0

for student in score:
  sum+=student

average=sum/len(score)
print(average)

# ------------------
numbers=[1,2,3,4,5]
result=[]

for i in numbers:
  if i%2==0: result.append(i)
  else:result.append(i*2)

print(result)

total=[num*2 for num in numbers if num%2==1]

print(total)