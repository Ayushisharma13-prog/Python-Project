print("========= STUDENT GRADE MANAGER =========")
menu=["Add Student","View all students","Calculate Average","Find Highest Score","Search Element","Delete Student","Edit Student","Show Pass/Fail","EXit"]
view=[]
marks=[]

def Add_stud():
    student=[]
    while True:
     n=input("Enter name of the student:")
     if n=="none":
        break
     m=int(input("Enter the number of student:"))
     student.append(n)
     student.append(m)
     marks.append(m)
     view.append((n,m))
     
    #  print(student)

def calc_avg():
   s=0
   for i in marks:
    s=s+i
   avg=s/len(marks)
   print(avg)

   


while True:
    for i, x in enumerate(menu):
        print(i+1,x)
    choice=int(input("Enter your choice from 1 to 9:"))
    match choice:
     case 1:
        Add_stud()
     case 2:
          print(view)
     case 3:
          calc_avg()
     case 4:
          marks.sort(reverse=True)
          print(marks[0])
     case 5:
          s=input("Enter the name of Student:").lower()
          print(view)
          for name, marks in view:
             if name.lower()==s:
                print(f"found it!!\n{name}-{marks}")
                break
          else:
                print("Student not in the list.")
     case 6:
            p=input("enter the name of student you want to delete:")
            for name, marks in view:
                if name==p:
                    print(p)
            view.remove((name,marks))
            print(view)
     case 7:
            while True:
             edit=input("Enter the name of student you want to edit:")
             if edit=="done":
                 break
             for name,marks in view:
                p=["Edit name","Edit marks"]
                for i, value in enumerate(p):
                    print(i+1,value)
                # while True:
                s=int(input("Enter what you want to edit:"))
                if s==3:
                    break
                match s:
                    case 1:
                        g=input("Enter name:")
                        if g=="none":
                            break
                        for name,marks in view:
                            view.remove((name,marks))
                            view.append((g,marks))
                            # print(view)
                    case 2:
                        h=int(input("Enter marks:"))
                        if h<0:
                            break
                        for name,marks in view:
                            view.remove((name,marks))
                            view.append((name,h))
                            # print(view)
            print(view)
            
            
     case 8:
            for i in marks:
                if i<23:
                    print("Fail")
                else:
                    print("Pass")
                print(i)
     case 9:
      break
          
          

          





# student=[]
# n=input("Enter name of students:")
# m=int(input("Enter the number of student:"))
# student.append(n)
# student.append(m)
# print(student)
