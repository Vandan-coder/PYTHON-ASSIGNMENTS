menu =  """
                   MENU
                
                JAY BHAVANI

            VADAPAV   30
            DABELI    30
            BHEL      65

"""
print(menu)
product_list = []
price_list = []

status = True
name = input("Enter your name :  ")
while status:
     product = input("Enter your product name :  ")
     product_list.append(product)
     if product=="VADAPAV" or product =="DABELI":
        price = 30
     else :
        price = 65
     qty = int(input("Enter no. of quantity you want : "))
     total_price = qty*price
     price_list.append(total_price)
     print(total_price)

     choice = input("If you want to add more product : Press Y for Yes OR Press N for No : ")
     if choice=="y" or choice=="Y":
      status = True
     else:
      status = False

count = 0 
for product in product_list:
    print(f"{product} =  {price_list[count]}")
    count +=1

print("GRAND TOTAL : ",sum(price_list))
