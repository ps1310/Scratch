import random

rand_int = random.randrange(0,21)
print("I've just generated a random integer between 0 and 20.")

while True:
    try:
        guess = int(input("Give me your best integer guess: "))
        
        while guess != rand_int:
            if guess > rand_int:
                guess = int(input("Your guess is too high, try again: "))
            elif guess < rand_int:
                guess = int(input("Your guess is too low, try again: "))

        print("You got it!")
        break

    except ValueError:
        print("That was NOT an integer!")