import random
import time

time.sleep(1)
print("Hello World!")

text = "Welcome to HangMan..."
lives = 10
guesses = []
timesplayed = 0
roundswon = 0
roundslost = 0

# Words

easy_words = ["cat", "dog", "sun", "tree", "fish", "book", "apple", "star", "bird", "milk", "cake", "ball", "moon", "hat", "rock", "rain", "car", "duck", "key", "pen"]

medium_words = ["garden", "window", "purple", "bridge", "pencil", "flower", "puzzle", "planet", "rocket", "bottle", "tiger", "candle", "dancer", "guitar", "breeze", "pirate", "jungle", "shadow", "ocean", "island"]

hard_words = ["quartz", "mystery", "awkward", "rhythm", "jigsaw", "zigzag", "vortex", "cryptic", "giraffe", "bizarre", "pharaoh", "dizzying", "whiskey", "gazelle", "mnemonic", "knapsack", "xylophone", "tsunami", "numbskull", "subtle"]

impossible_words = ["floccinaucinihilipilification", "antidisestablishmentarianism", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquipedaliophobia", "supercalifragilisticexpialidocious"]

# Game Code

def game():
    global timesplayed, lives, guesses, roundswon, roundslost

    # Select game mode
    while True:
        mode = input("What game mode would you like to play? (easy, medium, hard, impossible): ").lower()

        if mode == "easy":
            word = random.choice(easy_words)
            break
        elif mode == "medium":
            word = random.choice(medium_words)
            break
        elif mode == "hard":
            word = random.choice(hard_words)
            break
        elif mode == "impossible":
            word = random.choice(impossible_words)
            break
        else:
            print("Invalid mode. Please choose again.")

    guessed_word = ["_"] * len(word)
    lives = 10
    guesses = []
    timesplayed += 1

    # Main game loop
    while lives > 0 and "_" in guessed_word:
        print("\n=============================")
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Lives: {lives}")
        print("=============================\n")

        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a single letter.")
            continue

        if guess in guesses:
            print("\nYou've already guessed that letter.")
            continue

        guesses.append(guess)

        if guess in word:
            print(f"\nYay, you guessed '{guess}' correctly.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            lives -= 1
            print(f"You have {lives} lives left.")

    # Game outcome
    if "_" not in guessed_word:
        print(f"\nCongratulations! You've guessed the word '{word}' correctly!")
        roundswon += 1
    else:
        print(f"\nGame over! The word was '{word}'.")
        roundslost += 1

# Welcome message
time.sleep(1)
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)

print("\n")
time.sleep(1)
print(" The aim of the game is to: ")
time.sleep(1)
print("1. Type letters on the keyboard to try and find out the mystery word.")
time.sleep(1)
print("2. Gain points for beating the game.")
time.sleep(1)
print("3. If you run out of lives, you lose.")
time.sleep(1)
print("\nLet's Play...")

# Main loop to play again
while True:
    game()

    # Games Won / Total Games Played * 100
    if timesplayed > 0:
        winpercent = round((roundswon / timesplayed) * 100, 2)
    else:
        winpercent = 0

    with open("Scores.txt", "w") as file:
        file.write("Thank you for playing HangMan:\n")
        file.write(" You can look at more projects like this on my github profile:\n")
        file.write("\n")
        file.write("https://github.com/hippogriff101\n")
        file.write("\n")
        file.write("Thank you to arcade for the opportunity to advance my coding knowledge.\n")
        file.write("Find this on the repo called 'hangman'.\n")
        file.write("\n")
        file.write("Scores:\n")
        file.write("Times Played: {timesplayed}\n")
        file.write("Rounds Won: {roundswon}\n")
        file.write("Rounds Lost: {roundslost}\n")
        file.write("Win Percent: {winpercent}%\n")

    print("\n")

    playagain = input("Do you want to play again? (yes/no): ").lower()

    if playagain == "yes":
        continue
    elif playagain == "no":
        print("Thanks for playing!")
        print("\n")
        break
    else:
        print("Sorry, what's that?")
