
# contact book
dic = {
}

content = None
def func(name, number):
   dic.update({name : number})
   f = open("Contacts.txt", "a")

   #dup remove+++++++++++++++++++++++++++
   with open("Contacts.txt", "r") as w:
      file = w.readlines()
      for line in file:
          wordlist = []
          badlist = []
          wordlist.append(line)
          q=set()
          q.add(line)
      if q == wordlist:
          f.write(name + ": " + number + "\n")
          print("the contacts have been updated")
      else:
         for line in file:
            if line in wordlist:
               badlist.append(line)
            else:
               wordlist.append(line)
         print("it's already in the file")


   file = open("Contacts.txt", 'w')
   for line in wordlist:
      file.write(line)





while True:
   name = input("enter the name:  \n")
   number = input("enter the number: \n")
   func(name, number)
   x = input("do you want to add more?: Y/N \n").lower()
   if x != "y":
       break

