
Contacts = {}
p = ""
n = ""

with open("Contacts.txt","r") as f:
   file = f.readlines()
   for line in file:
      if line != "\n":
         line.strip("\n")
         key, value = line.split(':')
         key= key.strip()
         value= value.strip()
         Contacts[key] = value

while True:
   global x
   x = 0
   x = int(input("1_Add new contact\n2_Remove a contact\n3_Edit number\n4_View contacts\n5_Search a name\n6_Exit\n"))



   # ADD NEW
   if x == 1:
      Contacts.update({input("please enter the name: "):input("enter the number: ")})


   # REMOVE
   elif x == 2:
      Contacts.pop(input("enter the name you want to be removed: \n"))


   # EDIT
   elif x == 3:
      try:

         Contacts[input("Enter the contact's name whos number you want to edit: \n")] = int(input("Enter a number: \n"))
      except:
         print("Contact name does not exist")


   # VIEW
   elif x == 4:
      print("----------")
      for i in Contacts:
         print(i)
         print(Contacts[i])
         print("----------")


   # Search??
   # if the input is in the dictionary show the key and value
   elif x == 5:
      c = input("enter the name you want to view")
      if c in Contacts:
         print(c)
         print(Contacts[c])


   # EXIT (else it if no more options dont forget)
   elif x == 6:
      if input("Are you sure?: Y/N \n").lower() == "y":
         f = open("Contacts.txt", "w")
         for i in Contacts:
            f.write(i + ":" + str(Contacts[i] + "\n"))
         f.close()
         break
      else:
         pass


   #write
   f = open("Contacts.txt","w")

   for i in Contacts:
      f.write(i + ":" + str(Contacts[i]+ "\n"))



   f.close()

   # make a function to return "y" if it agrees to continue else it will set to non y and
   # this prompt will not come back
   if input("Continue?: Y/N \n").lower() != "y":
      break



