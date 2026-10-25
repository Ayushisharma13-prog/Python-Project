User_pin=237890
Menu=["Check Balance", "Deposit Money", "Withdraw Money","Transaction History","Change PIN","Exit"]
balance=50000
transaction=[]
dl=20000
Aw=0

PIN=int(input("Enter Your Validated PIN please: "))
PIN_limit=0

def check_balance():
    print(balance)

def depo_m(balance):
   while True:
    # for i in range (0,3):
     d_a=int(input("Enter amount for deposit:"))
     
     if d_a<500:
      print("Insufficient Amount.") 
      continue
     else:
      balance=balance+d_a
      print(balance)
      transaction.append(f"Deposited {d_a}")
     return balance

def withd_m(balance,Aw):
   while True:
    w_a=int(input("Enter your withdrawal amount:"))
   
    if w_a<1:
      print("Insufficient Amount")
      continue
    elif w_a>balance:
      print("You don't have enough balance to withdraw.")
      continue
    elif Aw+w_a>dl:
      print("you can't withdraw this amount. You've reached your daily limit.")
      return balance,Aw
    
    else:
     Aw=Aw+w_a
     if w_a>1:
      transaction.append(f"Withdrawn {w_a}")
     balance=balance-w_a
    print(balance)
    return balance,Aw
   
def change_pin():
   int(input("Enter your current PIN:"))

   while True:
    new_pin=int(input("Enter Your New PIN:"))
    confirm_pin=int(input("Enter Your PIN to confirm:"))

    if new_pin==confirm_pin:
     print("PIN changed succesfully.")
     break
    else:
      print("This isn't same as above.")
      continue
    
def trans_hist():
  print("----------------TRANSACTION HISTORY---------------------")

  if transaction==[]:
    print("No recent transaction history")
  else:
     print(transaction)

if PIN==User_pin:
    print("Welcome to PY bank ,moving you to the next step in few seconds!!")
else:
    print("Try again!!")

    for i in range(0,3):
        int(input("Enter your PIN again:"))
        PIN_limit=PIN_limit+1
        # if PIN_limit>3:
    print("You've exceeded your limit. Wait for a few seconds and getting back at you.")

while True: 
 for i, item in enumerate(Menu):
    print(i+1,item)

 choice=int(input("enter your preffered choice from menu from 1 to 6:"))
 match choice:
    case 1:
       check_balance()
    case 2:
       balance=depo_m(balance)
    case 3:
       balance,Aw=withd_m(balance,Aw)
    case 4:
     trans_hist()
    case 5:
       change_pin()
    case 6:
       break
       





