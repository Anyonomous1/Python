import random
Cch=random.randint(0,2)
Uch=int(input("Enter ur choice 0.Rock, 1.Paper or 2.Scissors : "))
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
items=["Rock","Paper","Scissors"]
if(Uch>=0 and Uch<3):
    print(f"{choice[Uch]} V/S {choice[Cch]}")
    print(f" => User_choice: {items[Uch]}  V/S  Computer_choice: {items[Cch]}")
    print("")
    if(Uch==0 and Cch==2):
        print("You have won \n")
    elif(Cch==0 and Uch==2):
        print("You have lost \n")
    elif(Uch>Cch):
        print("You have won \n")
    elif(Cch>Uch):
        print("You have lost \n")
    elif(Uch==Cch):
        print("Its a draw \n")
else:
    print("Play by the rules my guy \n")