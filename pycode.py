import random, time
list = ['rock', 'paper', 'scissors']
w = "You win!"
L = "You lost"
T = "Its a tie!"
play = True


#we start the game with taking the "user" input

def start():
    global play
    play = True
    while play == True:
        print("cool!")
        time.sleep(1)
        x = input("rock, paper, scissors? : ")
        if x in list:
            user = list.index(x)
        else:
            print("wrong input")
            break


         #opponent does their thing
        '''
        hoping to make the opponent action less random 
        meaning they wont reuse scissors if they 
        lost  with it or something like that
        '''

        opp = list.index(list[random.randint(0, 2)])
        for i in range(1, 4):
            print(i)
            time.sleep(0.7)
        print("opponent: ", list[opp])



        # winloss conditions
        # W,L,T were defined at the first few lines
        if user == 0 and opp == 2 or user == 1 and opp == 0 or user == 2 and opp == 1:
            time.sleep(1)
            print(w)
        elif user == opp:
            time.sleep(1)
            print(T)
        else:
            time.sleep(1)
            print(L)


#it shouldn't have worked but it did???
#replayabillity

        if input("replay?: Y/N \n ").lower() == "y":

            play = True
            start()
        else:

            play = False
            exit()


#   corny starting
#defined a func to use in start
def why():
    print("why did you come here then", end = "", flush = True)
dot = [".",".","."]


# this starts
if input("wanna play?: Y/N \n").lower() == "y":

   start()
   time.sleep(0.75)
else:
   why()
   for i in dot:
      time.sleep(0.5)
      print(i, end="")
   time.sleep(1)

   exit()



