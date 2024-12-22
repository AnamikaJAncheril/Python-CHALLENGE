print("WELCOME TO PIZZA ORDER SYSTEM")
size=input("What size pizza do you want  ?  S, M or L : ")
pepperoni = input("Do you want pepperoni on your pizza ? Y or N : ")
extra_cheese = input("do you want extra cheese ? Y or N :")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L" :
    bill += 30
else :
    print("you typed the wrong input ")

if pepperoni == "y" :
    if size == "S" :
        bill += 2
    else :  
        bill +=3
if extra_cheese == "Y" :
    bill += 2
else :
    bill += 1
print(f"your final bill is  : {bill}")