print("~~~~~~Welcome, to your Personal Expense Tracker!!~~~~~~")
categories=["Add Expense","View All Expenses","Total Spent","Highest Spent","Number of Expenses","Search expenses","Delete Expense","Edit Expense","Exit"]
view=[]
view1=[]
Expense=[]
total=0

# for i, category in enumerate(categories):
#     print(i+1,category)


def add_Expense():
    while True:
     expense=input("Enter your Expense:")
     if expense=="none":
        break
     Amount=int(input("Enter amount:"))
     if Amount<1:
        print("Invalid Amount.")
        int(input("Enter Amount:"))
     Expense.append(Amount)

     view.append(f"your Expense: {expense}\namount: {Amount}")
     view1.append((expense,Amount))

    

     print("Expense added sucessfully!!")
     

def total_spent(Expense):
      total=0
      for j in Expense:
         total=total+j
      print(total)
      print("The number of expenses:", len(Expense))
      print(Expense)

   
while True:
 for i, category in enumerate(categories):
    print(i+1,category)
 choice=int(input("Enter the number for the task from 1 to 9: "))
 match choice:
   case 1:
      add_Expense()
   case 2:
      for i in view:
         print(i)
   case 3:
       total_spent(Expense)
   case 4:
       Expense.sort(reverse=True)
       print(Expense)
       print(Expense[0])
   case 5:
       print("The number of expenses:", len(Expense))
   case 6:
       e=input("enter expense:").lower()
       print(view1)
       for name, amount in view1:                  #tuple unpacking
          if name.lowe()==e:
             print(f"found it!!\n{name}-₹{amount}")
             break
       else:
          print("Not found!!")
   case 7:
       d=input("Enter expense you want to delete:")
       for name,amount in view1:
          if name==d:
             print(d)
             view1.remove((name,amount))
             print(view1)
   case 8:
       edit=input("Enter expense you want to edit:")
       for name, amount in view1:
          if name==edit:
             t=["amount","name"]
             for i,p in enumerate(t):
                print(i+1,p)
             
             s=int(input("enter no. from 1 or 2: "))
             match s:
                case 1:
                   p=int(input("amount:"))
                   print((name,p))
                   view1.remove((name,amount))
                   print(view1)
                   view1.append((name,p))
                case 2:
                   i=input("name: ")
                   print((name,i))
                   view1.remove((name,amount))
                   view1.append((i,amount))
          print(view1)
   case 9:
       break
             

       

       
       
   
      