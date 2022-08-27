team1 = int(input("Enter team 1 score : "))
team2 = int(input("Enter team 2 score : "))
team3 = int(input("Enter team 3 score : "))
if team1>team2:
    if team1>team3:
        print("team1 is greater")
    else:
        print("team3 is winner")
else:
    if team2>team3:
        print("team2 is greater")
        
        