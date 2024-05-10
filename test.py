import string
a,b,c,d,e,f,g,h,p =  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '
boardx = [p, a,b,c,d,e,f,g,h]
boardy = [1,2,3,4,5,6,7,8]


print(boardx)
print(boardy)
for column in boardy[8::-1]:
    print(column)
for row in boardx[0::]:
    print(row, end="  ")


class board:
    def __init__(self, x, y):
        self.num = y
        self.let = x
    def place(self, x, y):
        print("enter the coordinates")
        x = input("enter x")
        y = input("enter y")
        boardx.index(x) = x
        boardy.index(y) = y

#queens should have their own coordinates but how do we place them on their own
q1= board(input("enter letter: "), input("enter number: "))
