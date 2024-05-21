
Contacts = {}

while True:
   global x
   x = 0
   x = int(input("1_Add new contact\n2_Remove a contact\n3_Edit number\n4_View contacts\n5_Exit\n"))

   #ADD NEW
   if x == 1:
      Contacts.update({input("please enter the name: \n"):int(input("enter the number: \n"))})
      print(Contacts)

   # REMOVE
   elif x == 2:
      Contacts.pop(input("enter the name you want to be removed"))

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


      '''
   # EXIT (else it if no more options dont forget)
   elif

   # I DONT KNOW MAN
   else
'''
   if input("Continue?: Y/N").lower() != y:
      break