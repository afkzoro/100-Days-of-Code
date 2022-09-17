#Using a Dictionary of values
import random
from game_data import data
from art import vs
from art import logo
import os

def higher_lower(list):
    flag = True 
    first_search = random.choice(list)
    score = 0
    print(logo)
    
    while flag != False:
        print(f"Compare A: {first_search['name']}, a {first_search['description']}, from {first_search['country']}")
        first_value = first_search['follower_count']
        
        second_search = random.choice(list)
        if second_search == first_search:
            second_search = random.choice(list)
        
        print(vs)
        
        print(f"Against B: {second_search['name']}, a {second_search['description']}, from {second_search['country']}")
        second_val = second_search['follower_count']
        
        decide = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        def compare(val1, val2):
            if val1 > val2:
                return True
            elif val1 < val2:
                return False
        
        if decide == "A":
            if compare(val1=first_value, val2=second_val) == True:
                first_search = first_search
                score += 1
                #os.system('cls')
            elif compare(val1=first_value, val2=second_val) == 0:
                first_search = first_search
                score += 1
                 
            elif compare(val1=first_value, val2=second_val) == False:
                print(f"Sorry you lose. Final score is {score}")
                flag = False
                #os.system('cls')
                break
        
        elif decide == "B":
            if compare(val1=first_value, val2=second_val) == False:
                first_search = second_search
                score += 1
                #os.system('cls')
            elif compare(val1=first_value, val2=second_val) == True:
                os.system('cls')
                print(f"Sorry you lose. Fianl score is {score}")
                flag = False
                break
                
            

higher_lower(data)