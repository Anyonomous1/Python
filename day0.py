for i in range(1,5):
  print("\n")
  for j in range(1,6):
    print("*" *j)


#better
for i in range(1,25):
  print("* "*i)


import random
c=0
die1=random.randint(1,6)
die2=random.randint(1,6)
total=die1+die2
while(total !=2):
  print("Nope")
  if(c==1):
    break
  c+=1
  print("Nope")
print("snake eyes")





answer=(input("Are we there yet? "))
while answer!="Yes":
  answer=input("Are we there yet? ")
