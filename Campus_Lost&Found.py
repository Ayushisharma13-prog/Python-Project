print("_________________CAMPUS LOST AND FOUND______________")

list=["Report lost item","Report Found item","View All items","Search Item", "Update Item","Exit"]

li=[]
fi=[]
# item={}
def lostitem():
    c=int(input("Enter no. of items needs to be reported:"))
    
    for k in range(0,c):
         l=["Item Name","category","location","Date","Description","person Name","Status"]
         item={}
         for i in l:
       
             if i=="Status":
                 #   print(i)
                 item[i]="lost"

             else:
                 print(i)
                 k=input(f"Enter {i}:")
                 item[i]=k
         li.append(item)

    print(li)



def founditem():
    d=int(input("Enter no. of items need to be reported:"))
    
    for i in range(0,d):
         l=["Item Name","category","location","Date","Description","person Name","Status"]
         items={}
         for j in l:
              if j=="Status":
                 items[j]="Found"
              else:
                 print(j)
                 s=input(f"Enter {j}:")
                 items[j]=s
         fi.append(items)

    print(fi)


def viewitems():
    h=["Lost Items","Found Items","Both"]
    for p,z in enumerate(h):
        print(p+1,z)
    choice=int(input("enter your choice for h:"))
    match choice:
        case 1:
            print(li)
        case 2:
            print(fi)
        case 3:
            print(f"Lost Items:- {li}")
            print(f"Found Items:- {fi}")



def Searchitem():
    l=input("Enter Item:")
    found="False"
    for i in li:
        if i["Item Name"].lower().strip()==l.lower().strip():
            # print(i)
            print("This item has been reported lost.")
            print(i)
            found="True"
    for i in fi:
        if i["Item Name"].lower().strip()==l.lower().strip():
            # print(i)
            print("This item has been reported found.")
            print(i)
            found="True"

    if found=="False":
        print("Item not found.")


def updateitems():
    n=input("enter item you want to update:")
    found=False
    for i in li:
        if i["Item name"]==n:
            found=True
            u=["Location","Person Name","Description","Status"]
            for a,b in enumerate(u):
                print(a+1,b)
            g=int(input("What you want to update:"))
            match g:
                case 1:
                    up=input("Enter new Location:")
                    i.update({"Location": up})
                case 2:
                    up=input("Enter Person Name:")
                    i.update({"Person Name": up})
                case 3:
                    up=input("Enter new Description:")
                    i.update({"Description": up})
                case 4:
                    up=input("Enter Status:")
                    i.update({"Status": up})
            print("Item Updated Succesfully!!")
            print(i)


    for i in fi:
            if i["Item name"]==n:
                found=True
                u=["Location","Person Name","Description","Status"]
                for a,b in enumerate(u):
                    print(a+1,b)
                g=int(input("What you want to update:"))
                match g:
                    case 1:
                        up=input("Enter new Location:")
                        i.update({"Location": up})
                    case 2:
                        up=input("Enter Person Name:")
                        i.update({"Person Name": up})
                    case 3:
                        up=input("Enter new Description:")
                        i.update({"Description": up})
                    case 4:
                        up=input("Enter Status:")
                        i.update({"Status": up})
                print("Item Updated Succesfully!!")


    if found==False:
        print("Item not found")



while True:
    for i,l in enumerate(list):
        print(i+1,l)
    choice=int(input("Enter your choice:"))

    match choice:
        case 1:
            lostitem()
        case 2:
            founditem()
        case 3:
            viewitems()
        case 4:
            Searchitem()
        case 5:
            updateitems()
        case 6:
            break



