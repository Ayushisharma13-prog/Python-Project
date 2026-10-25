import random
n=random.randint(1,100)
print("Guess a number between 1 to 100")
# print(n)
# while True:
#   menu=["Start Game","Exit Game","Play again"]
#   for i,v in enumerate(menu):
#    print(i+1,v)
def play_again():
   start_game()

name=input("Enter your name for the game:")

# attempt=0
def start_game():
 attempt=0
 while attempt<7:
    
    try:
        number=int(input("enter number:"))
        attempt=attempt+1
    except ValueError:
        print("Please Enter a integer number:")
        break

    if n>100:
        print("Too High.")
    elif n<1:
        print("Too Low.")
    elif n==number:
        print(f"Absoulutely, right guess {name}")
        break
 else:
    print("You only get 7 attempts. Play again!!")
    print("Do you want to play again:")       
    p=input("tell yes or no:")
    if p=="yes":
       start_game()

while True:
  menu=["Start Game","Exit Game"]
  for i,value in enumerate(menu):
   print(i+1,value)
  choice=int(input("Enter what you want to do:"))
  match choice:
      case 1:
         start_game()
         print(n)
         
      case 2:
         break
     

