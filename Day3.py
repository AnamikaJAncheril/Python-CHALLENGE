print("WELCOME TO ROLLERCOSTER !")
print("*************************")
height=int(input("Enter your height in centimeters :"))
if height >= 120 :
    print("you can ride  the rollercoster")
    age=int(input("what is your age :"))
    if age >= 18 :
        print("please pay $12 !")
    else :
        print("please pay $7 !")
else :
    print("Sorry you can't ride the rollercoster ")
