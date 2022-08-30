import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)


chosen_word = random.choice(word_list)

print(f"Solution is {chosen_word}")

#Length
length = len(chosen_word)

dash = []

for i in range(length):
    dash.append("_")
game_loop = False

lives = 6
while game_loop != True:
    #User's guess
    guess = input("Guess a letter: ").lower()
    
    for i in range(length):
        letter = chosen_word[i]
        
        if guess in dash[i]:
            print("You've already guessed this letter.Try again!")
            break
        
        if letter == guess:
            dash[i] = letter
        
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
    print(stages[lives])
    print(f"{' '.join(dash)}")
    
    
    if "_" not in dash and lives > 0:
        game_loop = True
        print("You Win!")
    if lives == 0:
        game_loop = True
        print("You Lose!")
