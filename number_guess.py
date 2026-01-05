#this is a number guessing game. you set an upper limit and the computer selects a random number between 1 and that limit. The player has to guess the number. 
import random
top_of_range = input("Enter the upper limit for the number guessing game: ")
if top_of_range.isdigit():
     top_of_range = int(top_of_range)
     if top_of_range <=0:
         print("please enter a number larger than 0 next time.")
else :
    print("please enter a number next time.")

random_number = random.randint(1,top_of_range)
guesses = 0

while True:
    Guess=input("guess a number ")
    if Guess.isdigit():
        Guess = int(Guess)
    else:
        print("please enter a number next time.")
        continue
    guesses += 1
    if Guess == random_number:
        print("you got it right!")
        break
    elif Guess > random_number:
        print("you are above the number")
    else:
        print("you are below the number")
print("you got it in", guesses, "guesses")