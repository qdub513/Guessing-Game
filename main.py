print('hello...')
import random

name = input("What is your name?")
print("Do you want to play a game," + name + "?")
print("think of a number between 1 and 100.")
print("don't lose. this is a dangerous game")

my_number = random.randint(1, 100)
guesses = []
for guess_number in range(1,6):
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
        print("TOO LOW. uh oh. watch out")
      
    elif user_guess < my_number and difference < 10:
        print("a bit too low. you're almost there")
    elif user_guess > my_number and difference > 10:
        print("TOO HIGH. quit smoking")
    elif user_guess > my_number and difference < 10:
        print("a bit too high. coming down")
    else:
      break

if user_guess == my_number:
  print("You won " + name + "! You guessed my number in " + str(guess_number) + "guesses!")
  print("Your guesses were: " + " ".join(str(x) for x in guesses))
  
else:
  print("You big dummy! The number I was thinking of was " + str(my_number))
  
#test commit