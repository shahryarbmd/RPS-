
# contact book
dic = {
}

def func(name, number):
   dic.update({name : number})
   f = open("Contacts.txt", "a")

   if {name: number} in open("Contacts.txt", "r"):
      print("it's already in there mate")
   else:
      f.write(name + ": " + number + "\n")
      print("the contacts have been updated")


while True:
   name = input("enter the name:  \n")
   number = input("enter the number: \n")
   func(name, number)
   x = input("do you want to add more?: Y/N \n").lower()
   if x != "y":
       break

