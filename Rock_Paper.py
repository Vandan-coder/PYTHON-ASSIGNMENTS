import random

status = True
game_list = ["ROCK","PAPER","SCISSOR"]
u_score =0 
c_score = 0
while status:
    user = input("Enter your choice (ROCK OR PAPER OR SCISSOR) ").upper()
    computer = random.choice(game_list)
    print("COMPUTER CHOICE = ",computer)
    if user==computer:
       print("TIE")
    elif user=="ROCK" and computer=="PAPER":
       print("COMPUTER WON")
       c_score+=1 
    elif user=="ROCK" and computer == "SCISSOR":
       print("USER WON")
       u_score += 1
    elif user=="PAPER" and computer=="ROCK":
       print("USER WON")
       u_score += 1
    elif user=="PAPER" and computer == "SCISSOR":
       print("COMPUTER WON")
       c_score += 1
    elif user=="SCISSOR" and computer=="ROCK":
       print("COMPUTER WON")
       c_score += 1
    elif user=="SCISSOR" and computer == "PAPER":
       print("USER WON")
       u_score += 1

    choice = input("If you want to play again : Press Y for countinue OR Press N for Leave the game : ")
    if choice=="y" or choice=="Y":
      status = True
    else:
      status = False
print("USER SCORE =  ",u_score)
print("COMPUTER SCORE = ",c_score)           
