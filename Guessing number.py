import time

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


