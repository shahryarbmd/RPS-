import random, time


'''
ask for the choice
roll
show

can use decorators

a function that takes the x and uses the Dice setting to roll
'''
D = 0
q = True

#----------------------------------------------------------------------------------------------
#                                             function section
#----------------------------------------------------------------------------------------------

# REROLL------------------------------------------------------------------
def reroll(D,Sides):


   D = random.randrange(int(Sides))

   if D == 0:
      while D == 0:
        D = random.randrange(int(Sides))
        if D != 0:
          break
   print("--Rolled {}--".format(D))

#ROLL-----------------------------------------------------------------------------
def Dice(Sides):
   global q
   #make sure it wont bug out again by setting Sides to atleast 2
   Sides = int(Sides)
   Sides += 1
   if Sides == 1:
      Sides += 1
      print("dont do that again")


   # rolling happens----
   while q == True:

      D = random.randrange(int(Sides))

      if D == 0:
         while D == 0:
            D = random.randrange(int(Sides))
            if D != 0:
               break

      # outputs the result of roll
      time.sleep(0.1)
      print("--Rolled {}--".format(D))
      time.sleep(0.4)

      #REROLL
      while True:
         time.sleep(0.2)
         if input("Reroll?: Y/N \n").lower() == "y":
            reroll(D,Sides)
            time.sleep(0.4)
         else:
            break
      if input("Change the dice?: Y/N \n").lower() == "y":
         Dice(input("Enter your dice Sides(number): \n"))

      else:
         q = False


#----------------------------------------------------------------------------------------------
#                                      function section ended
#----------------------------------------------------------------------------------------------

# start the engine !
try:

   Dice(input("Enter your dice Sides(number): \n"))
   time.sleep(0.5)
except ValueError:
   print("you didnt enter a number")

