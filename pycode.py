import random, time
list = ['rock', 'paper', 'scissors']
w = "You win!"
L = "You lost"
T = "Its a tie!"
play = True

rw = 0
rt = 0
rl = 0
sw = 0
st = 0
sl = 0
pw = 0
pt = 0
pl = 0
r = 0
#we start the game with taking the "user" input

def start():
    global play, rw, rt, rl, sw, st, sl, pw, pt, pl, r

    play = True
    while play == True:


        time.sleep(1)
        x = input("rock, paper, scissors? : ")
        if x in list:
            user = list.index(x)
        else:
            print("wrong input")
            break


         #opponent does their thing




        opp = list.index(list[random.randint(0, 2)])
        if r==0:
           for i in range(1, 4):
              print(i)
              time.sleep(0.7)
           print("opponent: ", list[opp])
        if (rw+rt)/r >= 0.25:
           print("opponent: ", list[1])

        elif (sw+st)/r >= 0.25:
            print("opponent: ", list[0])

        elif (pw+pt)/r >= 0.25:
            print("opponent: ", list[2])
        else:
            print("opponent: ", list[opp])
        r += 1




         # _______WIN CONDITIONS_______

         #rock WIN if+

        if user == 0 and opp == 2:
           rw += 1
           time.sleep(1)
           print(w)

         #rock TIE
        if user == 0 and opp == 0:
           rt += 1
           time.sleep(1)
           print(T)

         #rock LOSE
        if user == 0 and opp == 1:
           rl += 1
           time.sleep(1)
           print(L)




        #scissor WIN if++
        if user == 2 and opp == 1:
           sw +=1
           time.sleep(1)
           print(w)

         #scissor TIE
        if user == 2 and opp == 2:
           st +=1
           time.sleep(1)
           print(T)

         #scissor LOSE
        if user == 2 and opp == 0:
           sl += 1
           time.sleep(1)
           print(L)


        #paper WIN if+++
        if user == 1 and opp == 0:
           pw +=1
           time.sleep(1)
           print(w)

         #paper TIE
        if user == 1 and opp == 1:
           pt += 1
           time.sleep(1)
           print(T)

         #paper LOSE
        if user == 1 and opp == 2:
           pl += 1
           time.sleep(1)
           print(L)
        print(rw)
        print(r)



#replayabillity_______________________________________________

        if input("replay?: Y/N \n ").lower() == "y":

            play = True

            start()
        else:

            play = False
            print("total games: ", r)
            print("games won: ", rw + sw + pw)
            print("games lost: ", rl + sl + pl)
            exit()


#   corny starting
#defined a func to use in start__________________________________
def why():
    print("why did you come here then", end = "", flush = True)
dot = [".",".","."]


# this starts
if input("wanna play?: Y/N \n").lower() == "y":
   print("cool!")

   start()
   time.sleep(0.75)
else:
   why()
   for i in dot:
      time.sleep(0.5)
      print(i, end="")
   time.sleep(1)

   exit()



