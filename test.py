import random, time
list = ['rock', 'paper', 'scissors']
w = "You win!"
L = "You lost"
T = "Its a tie!"
play = True
user = ""
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

class MyClass:
    def __init__(self, user, opp):
        self.user = user
        self.opp = opp

    def inp(self):
        pass

    def opp_inp(self):
        opp = random.choice(list)
        if r==0:
           for i in range(1, 4):
              print(i)
              time.sleep(0.7)
           print("opponent: ", list[opp])
        elif (rw+rt)/r >= 0.25:
           print("opponent: ", list[1])

        elif (sw+st)/r >= 0.25:
            print("opponent: ", list[0])

        elif (pw+pt)/r >= 0.25:
            print("opponent: ", list[2])
        else:
            for i in range(1, 4):
                print(i)
                time.sleep(0.7)
            print("opponent: ", list[opp])
        r += 1
    def win(self,user,opp):
        global rw, sw, pw

        #rockw
        if user == 0 and opp == 2:
           rw += 1
           time.sleep(1)
           print(w)

        #scissorw
        if user == 2 and opp == 1:
           sw +=1
           time.sleep(1)
           print(w)

        #paperw
        if user == 1 and opp == 0:
           pw +=1
           time.sleep(1)
           print(w)
        else:
            self.tie(self,user, opp)

    def tie(self,user,opp):
        global rt,st,pt

        #rockt
        if user == 0 and opp == 0:
           rt += 1
           time.sleep(1)
           print(T)

        #scissort
        if user == 2 and opp == 2:
           st +=1
           time.sleep(1)
           print(T)

        #papert
        if user == 1 and opp == 1:
           pt += 1
           time.sleep(1)
           print(T)
        else:
            self.lose(self, user, opp)

    def lose(self,user,opp):
        global sl,pl,rl

        # rock LOSE
        if user == 0 and opp == 1:
            rl += 1
            time.sleep(1)
            print(L)

        # scissor LOSE
        if user == 2 and opp == 0:
           sl += 1
           time.sleep(1)
           print(L)

        # paper LOSE
        if user == 1 and opp == 2:
            pl += 1
            time.sleep(1)
            print(L)
def start():
    global play, rw, rt, rl, sw, st, sl, pw, pt, pl, r, user
    play = True
    while play == True:
        x = input("rock, paper, scissors?: ")
        time.sleep(1)
        if x in list:
            user = list.index(x)
        else:
            print("wrong input")
            break
    use = MyClass()

    use.inp()


         #opponent does their thing








         # _______WIN CONDITIONS_______
    w = MyClass
    w.win()


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



