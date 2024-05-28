import random

#D6
'''
ask for the choice
roll
show

can use decorators

a function that takes the x and uses the Dice setting to roll
'''


def Dice(Sides):
   q = True
   while q == True:

      D = random.randrange(int(Sides))
      if D != 0:
         print("Rolled {}".format(D))
         q = False
      else:
         pass

while True:
   try:
      Dice(input("Enter your dice Sides(number): \n"))
   except ValueError:
      print("you didnt enter a number")
   #x = input("Choose your dice: \n 1_D6 \n2_D8\n3_D12\n4_D14\n5_D16\n6_D18\n7_D20")

   #if x == 1:
