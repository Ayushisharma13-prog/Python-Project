print("welcome to,KAUN BANEGA CROREPATI..")

print(" the question1 for today's episode is right on your computer screen.")

Questions=[" 1. What is the largest planet in our solar system?","2. Which Indian state hosted the SAFF Women's Championship 2026, which was won by India?","3. Who founded the Maurya Empire?","4. Who is known as the 'Flying Sikh' of India?"]

options=["A.MARS\nB.JUPITER\nC.MERCURY\nD.VENUS","A.MAHARASHTRA\nB.KERALA\nC.TELANGANA\nD.GOA","A.AKBAR\nB.CHANDRAGUPTA MAURYA\nC.CHANAKYA\nD.HUMANYU","A.MILKHA SINGH\nB.NEERAJ CHOPRA\nC.SUNIL CHEETRI\nD.LAKSHYA"]
c=["B","D","B","A"]
prizes=[10000,20000,40000,70000]
total=0
index=0
for i in Questions:
    print(i)
    print(options[index])
    a=input("enter answer:")
    if a in c[index]:
        print("correct answer.")
        total=total+prizes[index]
        print(total)
        index+=1
       
    else:
        print("wrong answer.")
print(total)


for i in options:
     print(i)
print(Questions[0])
print(options[0])

Answer=input("tell your answer to the computer:")


def amount(A):
     return A+amount
# for a in amount:
if Answer=="A":
     print("sahi jawab")
    #  amount=int(amount)
    #  amount=+10000
     a=amount(+10000)
else:
    print("better luck next time!")
print(a)


print(Questions[1])
print(options[1])

Answer=input("tell your answer to the computer:")

if Answer=="D":
     print("sahi jawab")
     amount=int(amount)
     amount=+20000
     a=amount(+20000)

else:
    print("better luck next time!")

print(a)

print("welcome to,KAUN BANEGA CROREPATI..")

print(" the question1 for today's episode is right on your computer screen.")

Questions=[" 1. What is the largest planet in our solar system?","2. Which Indian state hosted the SAFF Women's Championship 2026, which was won by India?","3. Who founded the Maurya Empire?","4. Who is known as the 'Flying Sikh' of India?"]

options=["A.MARS\nB.JUPITER\nC.MERCURY\nD.VENUS","A.MAHARASHTRA\nB.KERALA\nC.TELANGANA\nD.GOA","A.AKBAR\nB.CHANDRAGUPTA MAURYA\nC.CHANAKYA\nD.HUMANYU","A.MILKHA SINGH\nB.NEERAJ CHOPRA\nC.SUNIL CHEETRI\nD.LAKSHYA"]

c=["B","D","B","A"]
amount=0

print(Questions[0],"\n", options[0])
a=input("enter answer:")
if a in c[0]:
    print("correct answer.")
    amount+=10000
else:
    print("wrong answer.")
print(amount)

print(Questions[1],"\n", options[1])
a=input("enter answer:")
if a==c[1]:
    print("correct answer.")
    amount+=20000
else:
    print("wrong answer.")
print(amount)