print("Welcome to Ayura's Supermarket")
items=[('Rice       20kg'),('Milk       50kg'),('Lentils    100kg'),('Sugar      54kg'),('Salt       20kg'),('Exit')]
name=input("Enter your good name please:")
print("      Welcome",name)
print("==========GROCERY MENU===========")
index =0
# for i, items in  enumerate(items):
#   print(i+1,items)

while True:
  for i, item in  enumerate(items[0:6]):
    print(i+1,item)
  
  n=int(input("enter you choice from 1 to 5:")) 
  if n==6:
      break
  q=input("How much do you want:")

  match n:
    case 1:
      print(f"{q}kg Rice")
    case 2:
      print(f"{q}kg Milk")
    case 3:
      print(f"{q}kg Lentils")
    case 4:
      print(f"{q}kg Sugar")
    case 5:
      print(f"{q}kg Salt")
  # if n==6:
  #   break
# price(q)

    
   

    
