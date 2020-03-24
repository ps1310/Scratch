import pandas as pd
import random
from PIL import Image, ImageDraw

word_import = pd.DataFrame(pd.read_csv(r"C:\Users\peter\Downloads\Words.csv"))
word_import = word_import.values

word_select = random.choice(word_import)
print(word_select)
print(len(word_select[0]))
guess_count = 0

def split(word):
    return list(word)

print("Let's play Hangman!")
print("""You have 6 total attempts to guess the full word. 
Correct guesses do not add to your attempt count.""")
print("Let's get started!\nYour word is", len(word_select[0]), "letters long!")

letter_key = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                      "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
    try:
        guess = str(input("What's your first guess?: ")).upper()
        
        while len(guess) != 1 or guess not in letter_key:
            print("Please make sure you enter a valid single letter.")
            guess = str(input("So what's your next guess?: "))
        
        word_check = split(word_select[0])
        word_out = ['']*len(word_check)
        
        while guess_count < 7:
            if word_check == word_out:
                print("Congratulations, you won!")
                print("Your word is: ", word_check)
                break
            elif guess in word_check:
                word_out = [w if w == w2 or guess == w else '' for w, w2 in zip(word_check, word_out)]
                if word_check == word_out:
                    print("Congratulations, you won!")
                    print("Your word is: ", word_check)
                    break
                print("Good guess, here's what you have so far: ")
                print(word_out)
                print("You've used", guess_count, "guesses so far.")
                guess = str(input("So what's your next guess?: ")).upper()
                while len(guess) != 1 or guess not in letter_key:
                    print("Please make sure you enter a valid single letter.")
                    guess = str(input("So what's your next guess?: ")).upper()
            else:
                print("Sorry, that letter isn't in the word we're looking for!")
                print("Here's what you have so far: ")
                print(word_out)
                guess_count += 1
                print("You've used", guess_count, "guesses so far.")
                guess = str(input("So what's your next guess?: ")).upper()
                while len(guess) != 1 or guess not in letter_key:
                    print("Please make sure you enter a valid single letter.")
                    guess = str(input("So what's your next guess?: ")).upper()

        break

    except ValueError:
        print("Please make sure you use single letter inputs.")