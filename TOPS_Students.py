import random

candidates =  ["vandan","bhaumik","avi","kevin","Manish","devang","Zaid","Kabir","Karan","Rajbir","Basarat","Bhoomi"]

status = True
while status:
    person = random.choice(candidates)
    print("PERSON :  "+person)
    candidates.remove(person)
    print("CANDIDATES : ------",candidates)
    choice = input("Play again : ")
    if choice=="n" or choice=="N":
        status = False