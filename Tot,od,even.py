# Accept five subjects and marks from user

eve = 0
od = 0
for i in range(1,6):
    num = int(input("Enter a number :"))
    if num%2==0:
        print("Even numbers ")
        eve+= 1
    else:
        print("Odd numbers")
        od+= 1   
       

print("even tot = ",eve)
print("odd tot = ",od)            

    


    


 