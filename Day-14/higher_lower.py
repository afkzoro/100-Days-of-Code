#Using a Dictionary of values
from logging.config import valid_ident
import random
from game_data import data
from art import vs

def searchA(list):
    flag = True 
    first_search = random.choice(list, 1)
    score = 0
    
    while flag != False:
        print(f"Compare A: {first_search[0]['name']}, a {first_search[0]['description']}, from {first_search[0]['country']}")
        first_value = first_search[0]['follower_count']
        
        print(vs)
        
        second_search = random.choice(list, 1)
        print(f"Against A: {second_search[0]['name']}, a {second_search[0]['description']}, from {second_search[0]['country']}")
        second_val = second_search[0]['follower_count']
        
        decide = input("Who has more followers? Type A or B: ").upper()
        
        def compare(val1, val2):
            if val1 > val2:
                return True
            elif val1 < val2:
                return False
        compare(val1=first_value, val2=second_val)
        
        if decide == "A":
            if compare == True:
                score += 1
            elif compare == False:
                print("You lose")
                flag = True
                break
        
        elif decide == "B":
            if compare == False:
                first_search = second_search
                score += 1
            elif compare == True:
                print("You lose")
                flag = True
                break
                
            

searchA(data)