import random
rock = str('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = str('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = str('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

#Created list from literals
art = []
art.append(rock)
art.append(paper)
art.append(scissors)

#Generates random art
rand_art = random.sample(art, 1)[0]


choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.   ")

#For 0(rock)
if choose == "0" and rand_art == scissors:
 print(rock)
 print("Computer's choice")
 print(scissors)
 print("You win!")
 pass 

if choose == "0" and rand_art == paper:
 print(rock)
 print("Computer's choice")
 print(paper)
 print("You lose. Game over!")
 pass

if choose == "0" and rand_art == rock:
 print(rock)
 print("Computer's choice")
 print(rock)
 print("You lose. Game over!")
 pass

#For 1(Paper)
if choose == "1" and rand_art == rock:
 print(paper)
 print("Computer's choice")
 print(rock)
 print("You win!")
 pass 

if choose == "1" and rand_art == scissors:
 print(paper)
 print("Computer's choice")
 print(scissors)
 print("You lose. Game over!")
 pass 

if choose == "1" and rand_art == paper:
 print(paper)
 print("Computer's choice")
 print(paper)
 print("You lose. Game over!")
 pass 

#For 2(Scissors)
if choose == "2" and rand_art == paper:
 print(scissors)
 print("Computer's choice")
 print(paper)
 print("You win!")
 pass 

if choose == "2" and rand_art == rock:
 print(scissors)
 print("Computer's choice")
 print(rock)
 print("You lose. Game over!")
 pass 

if choose == "2" and rand_art == scissors:
 print(scissors)
 print("Computer's choice")
 print(scissors)
 print("You lose. Game over!")
 pass 

print("Play again some other time")