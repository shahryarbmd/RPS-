import random, time

choices = ["rock","paper","scissors"]
rw, rt, rl, pw, pl ,pt, sw, sl, st = 0, 0, 0, 0, 0, 0, 0, 0, 0
#r is total games
r = 0
player = None
computer = None
#class AI:  maybe maybe

def comp():
    global computer
    if r != 0:
        if pw+pt/r >= 0.333:
           computer = "scissors"
        elif rw+rt/r >= 0.333:
           computer = "paper"
        elif sw+st/r >= 0.333:
           computer = "rock"
    else:
        computer = random.choice(choices)



while True:
    #player
   player = input("rock paper scissors?: ")
   player = player.lower()

   #rule
   while player not in choices:
       player = input("rock paper scissors?: ")
       player = player.lower()

   #comp
   comp()

   #timed print                     PLAYER
   for i in range(1,4):
       print(i)
       time.sleep(0.75)
   print("player: ", player)

   #time print                      COMPUTER
   time.sleep(1)
   print("computer: ", computer)
   time.sleep(1.25)




   # rock
   if player == "rock":
       if computer == "scissors":
           rw += 1
           print("you win!")  #

       elif computer == "paper":
           rl += 1
           print("you lose!")  #

       elif computer == "rock":
           rt += 1
           print("it's a tie!")  #

   # paper
   elif player == "paper":
       if computer == "rock":
           pw += 1
           print("you win")
       elif computer == "scissors":
           pl += 1
           print("you lose!")
       elif computer == "paper":
           pt += 1
           print("it's a tie!")

   # scissors
   elif player == "scissors":
       if computer == "paper":
           sw += 1
           print("you win!")
       elif computer == "rock":
           sl += 1
           print("you lose!")
       elif computer == "scissors":
           st += 1
           print("it's a tie!")
   r += 1
   print(r)
   if input("do you want to play again? Y/N \n").lower() != "y":
       break
