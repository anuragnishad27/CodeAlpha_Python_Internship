print("Welcome to Hangman Game !")
print("Let's start learning Python.")

import random 
words = ["APPLE", "MANGO", "PYTHON", "TIGER", "GRAPES"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("============================")
print("     WELCOME TO HANGMAN     ")
print("============================")
print("Guess the hidden word, one letter at a time!")
print("You have 6 incorrect guesses. \n")

while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    print("incorrect gussess left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a single letter:").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("please enter only one letter.\n") 
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won")
        print("The word was:", secret_word)
        break 

    if wrong_guesses == max_wrong_guesses:
        print("\n Game Over")
        print("The Word was:", secret_word)
       
print("Thanks for playing Hangman!")            
