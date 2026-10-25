print("MINI LIBRARY MANAGER")
menu=("Add Book","View All Books","Search Books","Borrow Book","Return Book","Delete Book","Edit Book","Show Available Books","Library Statistics","Exit")
library={}
borr={}
status="Available"
def add_book():
   while True:
    bn=input("Enter name of the book:")

    if bn=="none":
      break
    elif bn==" ":
      print("book name not given")
      bn=input("Enter name of the book:")
    
    an=input("Enter name of the Author:")
    if an==" ":
      print("Author name not shared..")
      an=input("Enter name of the Author:")
      
    # status="Available"
    library[bn]=an,status
    print(library)


def view():
  for key,value in library.items():
    print(key,value)
  # print(library)


def search():
  a=input("Enter the name of book:").lower()
  if a.lower() in library:
    print("Book found!!")
    key,value=library[a]
    print(a,"-",key,value)
    print(library[a])
  else:
    print("Book not found!!")

def borrow():
  b=input("enter book:")
  if b in library:
    author,status=library[b]
    if status=="Available":
     print("We have the book.")
     n=input("Enter name of the borrower:")
     library[b]=( author,"Borrowed")
     borr[b]=author,n,"Borrowed"
     print(borr)
     print(library)
    else:
        print("book is already borrowed.")
  elif library=={}:
    print("No books exist in the folder.")
  else:
    print("book doesn't exist in library.")

def return_b():
  r=input("enter book:")
  p=input("enter borrower's name:")
  if r in borr:
    author,status=library[r]
    library[r]=( author,"Available")
    print(library)
    print(f"Thankyou {p}, for visiting us. ")
  elif r in library:
    print("The book hasn't been borrowed.")

def del_b():
  q=input("enter the name of book:")
  if q in library:
    # library.pop(q)
    # print(library)
    author,status=library[q]
    if (author,status)==(author,"Borrowed"):
      print("⚠️ Error!!")
  elif q in library:
    library.pop(q)
    print(library)
  else:
    print("We don't have the book.")


def edit_b():
  e=input("enter book you want to edit:")
  author,status=library[e]
  while True:
    f=["Book","Author name","Exit"]
    for i,v in enumerate(f):
      print(i+1,v)
    c=int(input("What do you want to change:"))
    match c:
      case 1:
        value=library[e]
        x=input("enter new book name:")
        library[x]=value
        print(library)
      case 2:
        author,status=library[e]
        h=input("Enter Your new author name:")
        library[e]=(h,status)
        print(library)
      case 3:
        break

# def avail_book():

while True:
  for i, m in enumerate(menu):
    print(i+1,m)
  choice=int(input("enter your choice from 1 to 10:"))
  match choice:
    case 1:
      add_book()
    case 2:
      view()
    case 3:
      search()
      #  case 4:
      #   borrow()
      #  case 5:
      #   return_b()
      #  case 6:
      #    del_b()
      #  case 7:
      #   edit_b()
    case 10:
      break
   
  
     










