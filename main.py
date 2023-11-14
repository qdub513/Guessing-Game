print('Wow, factual facts!')
import random

name = input("What it do baby! Name?")
print("Welcome to the mf guessing game," + name + "!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it sucka!")

my_number = random.randint(1, 100)
guesses = []
for guess_number in range(1,11):
    valid_guess = False
    while not valid_guess:
        try: 
            user_guess = int(input("Take a guess...\n"))
            valid_guess = True
        except ValueError: 
            print("Quit tripping and try again.")

    difference = abs(my_number - user_guess)
    guesses.append(user_guess)

    if user_guess < my_number and difference > 10:
        print("WAY TOO LOW BUD. try again")
      
    elif user_guess < my_number and difference < 10:
        print("Just a bit too low. try again")
    elif user_guess > my_number and difference > 10:
        print("WAY TOO HIGH BUD. try again")
    elif user_guess > my_number and difference < 10:
        print("Just a bit too high. try again")
    else:
      break

if user_guess == my_number:
  print("You won " + name + "! You guessed my number in " + str(guess_number) + "guesses!")
  print("Your guesses were: " + " ".join(str(x) for x in guesses))
  
else:
  print("You big dummy! The number I was thinking of was " + str(my_number))