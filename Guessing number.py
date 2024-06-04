import random,time,os
'''
need one empty slot for the number to switch rapidly and set to a random one between 1 and 20
then players guesses over and under while he sees the list of numbers plus the one chosen randomly
then
roll another number to decide if it is correct
if correct add a point if not remove the points

how to clear outputted messages
with /r

'''
point = 0

def over(num):
   pass

def under(num):
   pass

while True:
   if input("are you ready to start?: Y/N \n").lower() != "y":
       break
   else:
       print("good luck!")

   for i in range(1,21):

      print(i, end='\r')
      time.sleep(0.5)




