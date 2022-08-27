shopping_list = []
status=True

while status:
    product = input("Enter product : ")
    shopping_list.append(product)
    choice = input("Do you want to add more product : ")
    if choice=='n' or choice=='no':
        status=False

for item in shopping_list:
    print(item)        