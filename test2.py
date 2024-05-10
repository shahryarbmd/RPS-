import numpy as np, random
board = np.array([[1,2,3,4,5,6,7,8],['a','b','c','d','e','f','g','h']])
class myboard:
    def __init__(self,x,y):
        self.x = x

        self.y = y


    def puzzle(self,x,y ):
        x = board[1, x]
        y = board[0, y]
        out = [x, y]
        print(out)
#!!!!!!
# R is a random number between 0 and 8
# q2 is the letter we receive plus a random distance
    # NOTE
    '''
    while checks if q2 is inside our board to continue
    while also checks the rules
    '''  # NOTE OVER
    def seek(self, q):
        x = q.index(q[0])
        R = random(0,9)
        q2 = q[x + R, q[1] + R]

        while q2[0] in board[1] and q2[1] in board[0] and q[0] != q2[0] and q2[1] not  :
           #honestly idk maybe q3 goes here


#!!!!!!
#we need 8 queens

q1 = myboard(0,1)
y = q1.puzzle(int(input()), int(input()))
q1.seek(y)

'''
reminder
we need to get a queen, use it to make other queens while not breaking the rules

turn x from seek back to its letter value
'''


