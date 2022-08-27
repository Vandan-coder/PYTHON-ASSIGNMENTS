import random

main_list = []

while len(main_list)<12:
    ticket = random.randint(1,100)
    if ticket not in main_list:
        main_list.append(ticket)

player_1 = main_list[:6] # for first 6 elements from the list
player_2 = main_list[6:] # for last 6 elements from the list 

random.shuffle(main_list)
print(main_list)
print(player_1)
print(player_2)

ticket_list = main_list

print("LET'S START THE GAME")

status =  True
while status:
    input()
    lucky_ticket = random.choice(ticket_list)

    print("LUCKY NUMBER : ",lucky_ticket)
    if lucky_ticket in player_1:
        print("Player 1 Win ")
        player_1.remove(lucky_ticket)
    elif lucky_ticket in player_2:
        print("Player 2 Win")
        player_2.remove(lucky_ticket)
    print("Player 1 = ",player_1)      
    print("Player 2 = ",player_2)  
    ticket_list.remove(lucky_ticket)

    if len(player_1)==0:
        status = False
        print("------------- PLAYER 1 WON THE GAME ----------")
    elif len(player_2)==0:
        status = False
        print("------------- PLAYER 2 WON THE GAME ----------")

