print("============MINI EXPENSE MANAGER================")
menu=["Add Expense","View All Expenses","Search Expense","Total Expense","Highest Expense","Average Expense", "Summary","Delete an Expense","Exit"]
# for i,v in enumerate(menu):
#     print(i+1,v)
expense=[]
view=[]


def add_expense():
    while True:
     c=input("Enter expense:")
     if c=="none":
        break
    #  expense.append(c)
     view.append(c)
     amount=int(input("enter amount:"))
     if amount<1:
       print('Invalid amount')
       continue
     expense.append((c,amount))
     view.append(amount)
     print(expense)
     
    #  print(view)
     
def view_expense():
  print(view)


def search_expense():
  s=input("enter expense:")
  if s in expense:
    print("Found it")
  else :
    print("does not exist in it.")

def total_expense():
  sum=0
  for i,a in expense:
    print(a)
    sum=sum+a
    print("Total Expense = ", sum)
    
def highest_expense():
  am=[]
  for v,k in expense:
    print(k) 
    am.append(k)
    print(am)
    am.sort(reverse=True)
    print("Highest Expense = ",am[0])
    # am.sort)(reverse=True)
    # print(am[0]

def average_expense():
  add=0
  cg=[]
  for g,m in expense:
    cg.append(m)
    add=add+m
    aveg=add/len(cg)
    print("Average Expense = ",aveg)



def summary():
  for g,a in expense:
    print(g,"-","₹",a)
    

def delete_expense():
  d=input("enter expense you want to delete:")
  for b,v in expense:
    if b==d:
      print(d)
      expense.remove((b,v))
      print(expense)
  
while True:
   for i,v in enumerate(menu):
    print(i+1,v)
   choice=int(input("Enter no. between 1 to 9:"))
   match choice:
     case 1:
       add_expense()
     case 2:
       view_expense()
     case 3:
       search_expense()
     case 4:
       total_expense()
     case 5:
       highest_expense()
     case 6:
       average_expense()
     case 7:
       summary()
     case 8:
       delete_expense()
     case 9:
       break
   