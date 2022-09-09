import random

user_card = []
computer_card = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(num):
    rand_card = random.choices(cards, k=num)
    return rand_card

user_card.append(deal_card(2))
computer_card.append(deal_card(2))

flag = True
while flag != False:
    
    flat_user = []
    for sublist in user_card:
        for i in sublist:
            flat_user.append(i)
    

    flat_pc = []
    for sublist in computer_card:
        for i in sublist:
            flat_pc.append(i)

    
    def calculate_score(cards):
        score = sum(cards)
    
        #Blackjack check
        if score == 21:
            return 0
    
        if score > 21:
            for i in range(len(cards)):
                if cards[i] == 11:
                    cards[i] = 1
                    new_score = sum(cards)
                    return new_score
                else:
                    pass
        else:
            return score
    
    print(f"\tYour cards: {flat_user}, current score: {calculate_score(flat_user)}")
    print(f"\tComputer's first card: {flat_pc[0]}")
    
    if calculate_score(flat_user) == 0:
        print("You won")
        break
    elif calculate_score(flat_pc) == 0:
        print("You lose. The computer wins")
        break
    elif calculate_score(flat_user) > 21:
        print("You lose")
        break
    
    decide = input("Do you want to pull another card 'y' for yes or 'n' for no:  ")
    
    if decide == "y":
        user_card.append(deal_card(1))
    elif decide == "n": #Buggggggggggggggggggggggggg
        while calculate_score(flat_pc) < 17:
            computer_card.append(deal_card(1))
    
    sumUser = sum(flat_user) 