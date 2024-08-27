import random
import time

time.sleep(1)

print("Hello World!")

text = ("Welcome to HangMan...")
lives = 10
guesses = []
timesplayed = 0

#Words

easy_words = ["cat","dog","sun","tree","fish","book","apple","star","bird","milk","cake","ball","moon","hat","rock","rain","car","duck""key","pen"]

medium_words = ["garden", "window", "purple", "bridge", "pencil", "flower", "puzzle", "planet", "rocket", "bottle", "tiger", "candle", "dancer", "guitar", "breeze", "pirate", "jungle", "shadow", "ocean", "island"]

hard_words = ["quartz", "mystery", "awkward", "rhythm", "jigsaw", "zigzag", "vortex", "cryptic", "giraffe", "bizarre", "pharaoh", "dizzying", "whiskey", "gazelle", "mnemonic", "knapsack", "xylophone", "tsunami", "numbskull", "subtle"]

impossible_words = ["floccinaucinihilipilification", "antidisestablishmentarianism", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquipedaliophobia", "supercalifragilisticexpialidocious"]

# Game Code

def game():

    global timesplayed
    global lives
    global lives

    mode = input("What game mode would you like to play? (easy, medium, hard, impossible): ")

    if mode == "easy":
        word = random.choice(easy_words)
    elif mode == "medium":
        word = random.choice(medium_words)
    elif mode == "hard":
        word = random.choice(hard_words)
    elif mode == "impossible":
        word = random.choice(impossible_words)

    guess = input("Please guess a letter: ")
    timesplayed =+ 1

    len(word)

    if guess in word:
        print("Yay, you guess correctly.")
        guesses.append(guess)
    else:
        print("That's not right.")
        guesses.append(guess)
        lives =- 1
        print("You have",lives,"lives left.")


#Welcome

time.sleep(1)

for i in range(1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

    print(" ")
time.sleep(1)
print(" The aim of the game is to: ")
time.sleep(1)
print("")
time.sleep(1)
print("1. Type letters on the keybord to try and find out the mystery word.")
time.sleep(1)
print("2. Gain points for beating the game.")
time.sleep(1)
print("3. If you run out of hearts you loose.")
time.sleep(1)
print("Let's Play...")

while True:
    
    print(game)

    