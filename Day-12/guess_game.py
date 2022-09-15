import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
num = random.randrange(1,101)
print(num)


def easy():
 lives = 10
 print(f"You have {lives} attempts remaining to guess the number")
 while lives != 0:
  guess = int(input("Guess the number:  "))
  
  if guess > num:
   print("Too high")
   print("Guess again")
   lives -= 1
   print(f"You have {lives} attempts remaining to guess the number")
   
  elif guess < num:
   print("Too low")
   print("Guess again")
   lives -= 1
   print(f"You have {lives} attempts remaining to guess the number")
   
  elif guess == num:
   print("you win")
   break
   
def hard():
 lives = 10
 print(f"You have {lives} attempts remaining to guess the number")
 while lives != 0:
  guess = int(input("Make a guess:  "))
  
  
  if guess > num:
   print("Too high")
   print("Guess again")
   lives -= 1
   print(f"You have {lives} attempts remaining to guess the number")
  elif guess < num:
   print("Too low")
   print("Guess again")
   lives -= 1
   print(f"You have {lives} attempts remaining to guess the number")
  elif guess == num:
   print("YOU WIN")
   break

decide = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()

if decide == "easy":
 easy()
elif decide == "hard":
 hard()
 
