import os

#Auction Iterations
flag = False
i = 0
loop = 1

#Empty dictionary
auc_dic = {}

while flag != True and i < loop:
    name = input("Enter your name: ")
    bid = int(input("How much is your bid price: $"))
    
    auc_dic[name] = bid
    
    #To i 
    decide = input("Are there any other bidders? Yes or No:  \n").lower()
    
    if decide == "yes":
        os.system('cls')
        loop += 1
    
    elif decide == "no":
        os.system('cls')
        flag = True
    i += 1
  
max_key = max(auc_dic)
max_value = max(auc_dic.values())
print(f"The winner is {max_key} with a bid of ${max_value}")
