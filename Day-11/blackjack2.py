import random

#
user_card = []
computer_card = []

#
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choices(cards, k=2)
    return rand_card

#
user_card.append(deal_card())
computer_card.append(deal_card())

print(user_card)
print(computer_card)
