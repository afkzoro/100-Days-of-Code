import random
import os
from art import logo

def blackjack():
    print (logo)
    user_card = []
    computer_card = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card(num):
        rand_card = random.choices(cards, k=num)
        return rand_card

    #Appends the random value to the lists
    user_card.extend(deal_card(2))
    computer_card.extend(deal_card(2))


    flag = True #Flag keeps the loop going
    while flag != False:
        
        #Function to calculate sum of lists
        def calculate_score(cards):
            score = sum(cards)
    
            if score == 21:
                return 0
    
            for i in range(len(cards)):
                if cards[i] == 11:
                    if score > 21:
                        cards[i] = 1
                        new_score = sum(cards)
                        return new_score
                return score

        print(f"\tYour cards are {user_card}, current score is: {calculate_score(user_card)}")
        print(f"\tComputer's first card: {computer_card[0]}")
    
        if calculate_score(user_card) == 0:
            print("You win!")
            break

        elif calculate_score(computer_card) == 0:
            print("You lose. THe computer wins!")
            break

        elif calculate_score(user_card) > 21:
            print("You lose!")  
            break
    
        decide = input("Do you want to pick another card. if yes enter 'y' if no 'n': ").lower()

        if decide == "y":
            user_card.extend(deal_card(1))
        
        elif decide == "n":
            flag = False
            while calculate_score(computer_card) <= 17:
                computer_card.extend(deal_card(1))
            print(f"\tYour final hand is {user_card}, final score is {calculate_score(user_card)}")
            print(f"\tComputer's final hand is {computer_card}, final score is {calculate_score(computer_card)}")
             
            #Function to compare final scores if user typed 'n'   
            def compare(first_card, second_card):
                if calculate_score(first_card) == calculate_score(second_card):
                    print("Its a draw!")

                elif calculate_score(first_card) > calculate_score(second_card) and calculate_score(first_card) < 21:
                    print("You win!")
                
                elif calculate_score(second_card) > calculate_score(first_card) and calculate_score(second_card) < 21:
                    print("You lose!. The computer wins")
                    
                elif calculate_score(first_card) > 21 and calculate_score(second_card) < 21:
                    print("You Lose!")
                    
                elif calculate_score(second_card) > 21 and calculate_score(first_card) < 21:
                    print("You Win!")
                    
            compare(first_card=user_card, second_card=computer_card)
            
            
player = input("Do you want to play a game of black jack. If yes enter 'y' if no enter 'n'").lower()

loop = True

while loop != False:
    if player == "y":
        loop = False
        os.system('cls')
        blackjack()
    elif player == "n":
        loop = False
        print("Bye friend!")
    else:
        print("Please enter the correct option")