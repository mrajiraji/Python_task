str = "i am not a robot to do all i am human"
str1 = str.split()
dup =[]
dup_count = 0
for i in str1:
  if i not in dup:
    dup.append(i)
  else:
    dup_count=dup_count+1
print("Removed Duplicate words",dup)
print("Counted Duplicate words",dup_count)   
