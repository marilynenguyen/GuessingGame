from art import logo
import random


def guessing(random_number):
    guess = int(input("Make a guess : "))
    guess_right = True
    if guess == random_number:
        print("You guessed right! >:)")
        return guess_right
    elif guess > random_number:
        print("You guessed too high >:(")
        print("Guess again...")
        return not guess_right
    elif guess < random_number:
        print("You guessed too low >:(")
        print("Guess again...")
        return not guess_right


print(logo)
print("Welcome to the Number Guessing Game ! ")

print("I am thinking of a number between 1 and 100...")

number = random.randint(0, 100)
# print(number)

game_continue = True
attempts = 0

while game_continue:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if difficulty == "easy":
        attempts = 10
        print(f"For this level, you have {attempts} to guess the right number.")
        while attempts != 0 and not guessing(number, attempts):
            attempts -= 1
            print(f"\nYou have {attempts} chances left.")
        if attempts == 0:
            print("You lost, game will end")

        game_continue = False

    elif difficulty == "hard":
        attempts = 5
        print(f"For this level, you have {attempts} to guess the right number.")
        while attempts != 0 and not guessing(number, attempts) :
            attempts -= 1
            print(f"\nYou have {attempts} chances left.")
        if attempts == 0:
            print("You lost, game will end")

        game_continue = False

    else:
        print("Invalid input. Please try again !")

