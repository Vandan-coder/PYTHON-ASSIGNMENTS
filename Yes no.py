
status = True

while status:
    num = int(input("Enter a number :"))
    print(num)

    choice = input("do you want to continue press Y or dont want to continue press N : ")
    if choice=='Y':
        status = True
    else:
        status = False 