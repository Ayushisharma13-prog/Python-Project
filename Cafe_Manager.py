print("STARLIGHT CAFE")
m=["View Menu","Place Order","Calculate Bill","Search Item","EXit"]
menu={
        "Snacks":[("Sandwich",100),("Spring roll", 100),("Poha",50),("Maggi", 50),("Idli",60)],
        "Parathe":[("Allo Paratha",20),("Pyaaj Paratha", 20),("Plain Paratha",10),("Gaubhi Parantha",30),("Muli Paratha",40)],
        "Lunch":[("Chole Bhature",30),("Chole Kulche",30),("Veg Biryani",30),("Roti-Sabji",100),("Paneer nann",120)],
        "Meetha":[("Rasgulla",20),("Icecream",[10,20,30,40,100]),("Besan Ladoo",10),("Kheer",50),("Gajar Halwa",50)],
        "Drinks":[("Chocolate Milkshake",120),("Cold Coffee",150),("Mojito",70),("Shikanji",50),("Apple Juice",50)]
    }

def view_menu():
    # menu={
    #     "Snacks":[("Sandwich",100),("Spring roll", 100),("Poha",50),("Maggi", 50),("Idli",60)],
    #     "Parathe":[("Allo Paratha",20),("Pyaaj Paratha", 20),("Plain Paratha",10),("Gaubhi Parantha",30),("Muli Paratha",40)],
    #     "Lunch":[("Chole Bhature",30),("Chole Kulche",30),("Veg Biryani",30),("Roti-Sabji",100),("Paneer nann",120)],
    #     "Meetha":[("Rasgulla",20),("Icecream",[10,20,30,40,100]),("Besan Ladoo",10),("Kheer",50),("Gajar Halwa",50)],
    #     "Drinks":[("Chocolate Milkshake",120),("Cold Coffee",150),("Mojito",70),("Shikanji",50),("Apple Juice",50)]
    # }
    for i,(key,value)in enumerate(menu.items()):
      print(f"{i+1}. {key} - ₹{value}")
    c=input("enter your preference please:")
    if c=="Snacks":
        for i,(item,p) in enumerate(menu["Snacks"]):
          print(i+1,item,p)
    elif c=="Parathe":
        for i,(item,p) in enumerate(menu["Parathe"]):
          print(i+1,item,p) 
    elif c=="Lunch":
      for i,(item,p) in enumerate(menu["Lunch"]):
          print(i+1,item,p) 
    elif c=="Meetha":
      for i,(item,p) in enumerate(menu["Meetha"]):
        print(i+1,item,p) 
    elif c=="Drinks":
      for i,(item,p) in enumerate(menu["Drinks"]):
        print(i+1,item,p) 
    return menu

bill=[]


def place_order():
   print("Hello Mam/Sir how may I help you?") 
   O=[]
   p=[]
   while True:
     order=input("Enter what you want to order:")
    #  O.append(order)
     if order==" ":
        break
    #  O.append(order)
     found=False
     for i in menu.values():
        for item,price in i:
         if order.strip().lower()==item.strip().lower():
              found=True
              # O.append((order,price))
              # p.append(price)
              if item=="Icecream":
                 p=int(input("What price of do you want:"))
                 if p in price:
                    print(p)
                    O.append((item,p))
                    q=int(input("enter quantity:"))
                    print(f"Icecream X {p} = {q*p}")
                    # O.append((order,price))
                 else:
                    print("select the available price!!")
              else:
                quantity=int(input("enter quantity:"))
                print(f"{item} X {price}= {quantity*price}")
                # p.append(price)
                O.append((order,price))
                bill.append((order,price,quantity))
        
     if found==False:
        print("not Available")
   print("BILL:", bill)
   print(O) 


def calculate_bill():
   total=0
   for i,v,q in bill:
      print(f"{i} X {v}= {v*q}")
      mo=v*q
      total=total+mo
   print("Total Bill -", total)
      # money.append(mo)


def search_item():
   s=input("Enter item you want to search:")
   found=False
   for i in menu.values():
     for j,p in i:
       if s.strip().lower()==j.strip().lower():
         print("Found")
         print(f"{j} - ₹{p}")
         found=True
         break
     if found:
       break
   if found==False:
      print("Not found")
  
while True:
    for i,v in enumerate(m):
        print(i+1,v)
    choice=int(input("enter choice:")) 
    match choice:
        case 1:
            view_menu()
        case 2:
          place_order()
        case 3:
          calculate_bill()
        case 4:
          search_item()
        case 5:
          print("Thankyou for visiting Starlight Cafe!!")

        





    