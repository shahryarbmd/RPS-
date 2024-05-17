
# contact book

dic = {
}

content = None
def func(name, number):
   dic.update({name : number})

   f = open("Contacts.txt", "a")
   f.write(name + ": " + number + "\n")
   #dup remove+++++++++++++++++++++++++++
   with open("Contacts.txt", "r") as w:
      file = w.readlines()
   wordlist = []
   badlist = []

   for line in file:
      if line in wordlist:
         badlist.append(line)
      else:
         wordlist.append(line)
   #dup remove done----------------------

   # clean lines put in++++++++++++++++++
   file = open("Contacts.txt", 'w')
   for line in wordlist:
      file.write(line)


   print("the contacts have been updated")

#
while True:
   name = input("enter the name:  \n")
   number = input("enter the number: \n")
   func(name, number)
   x = input("do you want to add more?: Y/N \n").lower()
   if x != "y":
       break

print(dic)