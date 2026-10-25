print("========= MINI CONTACT BOOK ========")
options=["Add contacts","View all contacts","Search contact","Delete contact","Edit contact","count contact"]
# for i, v in enumerate(options):
#     print(i+1,v)

contact={}
def add_contact():
   while True: 
     n=input("Enter the name of your contact:")
     if n=="none":
       break
     e=input("enter their email id: ")
     while True:
      p=input("Enter their contact Number:")
      if len(p)!=10 or not p.isdigit():
        print("invalid number")
      else:
        break
     contact[n] = e, p
     print(contact[n])
     print(f"Name: {n}\nEmail: {e}\nPhone no. :{p}")
     
     print("Your Contact added up succesfully!!")


def view_contact():
  for key, val in contact.items():
    print(key,":",val)
#    for key, val in contact:
#     print(contact)



while True:
   for i, v in enumerate(options):
     print(i+1,v)
   choice=int(input("What do you chose fro no 1 to 6:"))

   match choice:
      case 1:
        add_contact()
      case 2:
         view_contact()
      case 3:
       s=input("Search Contact:")
       if s in contact:
         print("found it!!")
         print(contact[s])
       else:
         print("not found!!")
      case 4:
       d=input("enter the name of contact :")
       if d in contact:
        contact.pop(d)
        print(contact)
       else:
         print("Contact does not exist.")
      case 5:
       edit=input("Enter contact name you want to edit:")
       if edit in contact:
         while True:
          ch=["Name","Email","Phone no"]
          
          for i, n in enumerate(ch):
           print(i+1,n)
          k=int(input("Enter your choice from 1 to 3:"))
          if k==4:
            break
          match k:
           case 1:
             value=contact[edit]
             name=input("Enter name:")
             contact[name]=value
             contact.pop(edit)
             print(contact)


            #  contact.update("Name:" ,name)
            #  print(contact)
           case 2:
             e,p=contact[edit]
             email=input("Enter Email:")
             contact[edit]=email,p
             print(contact) 
           case 3:
             e,p=contact[edit]
             phone=int(input("Enter number:"))
             contact[edit]=e,phone
             print(contact)
         else: 
           print("invalid") 
      case 6:
       print(len(contact))

   