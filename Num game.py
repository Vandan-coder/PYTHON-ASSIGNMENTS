import random
computer = random.randint(1,100)

status = True
while status:
    user = int(input("Enter your number : "))
    print(user)
    if user>computer:
        print("HINT : guess lower number")
    elif user<computer:
        print("HINT  guess higher number")
    else:
        print("YOU GOT IT !!!!")

status = False        

choice = input("If you want to add more product : Press Y for Yes OR Press N for No : ")
if choice=="y" or choice=="Y":
      status = True
else:
      status = False      