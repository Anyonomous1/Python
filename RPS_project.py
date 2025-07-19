import random
user=int(input("Enter your choice 0.rock 1.paper 2.scissors: "))
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choice=[rock,paper,scissors]
comp=random.randint(0,2)
print(choice[user])
print(choice[comp])
if(user<=2 and user>=0):
    if(user==comp):
        print("Its a draw")
    elif(user==2 and comp==0):
        print("You won")
    elif(comp==2 and user==0):
        print("You lose")
    elif(comp>user):
        print("You lose")
    elif(user>comp):
        print("You won")
else:
    print("wrong Input")