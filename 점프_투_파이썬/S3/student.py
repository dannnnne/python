mark=[90,25,67,45,80]
number=0

# for i in mark:
#   number=number+1
#   if i>=60:
#     print("%s번 합격입니다." %number)
#   else:
#     print("%s번 불합격입니다." %number)
    

# for i in mark:
#   number=number+1
#   # if i>=60:
#   #   print("%s번은 합격입니다. 축하합니다." %number)
#   # else:
#   #   continue
#   if i<60:continue
#   print("%s번 축하합니다!" %number)

for number in range(len(mark)):
  if mark[number]<60:continue
  print("%d번 축하합니다!" %(number+1))