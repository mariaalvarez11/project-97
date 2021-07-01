import random

print("guess the number! game")

number = random.randint(1,9)
chances = 0
print("guess a number between 1 and 9: ")

while chances < 5: 
    guess = int(input("guess the number: "))

    if guess == number: 
        print("you guessed right! congrats :)")
        break

    elif guess < number:
        print("your guess was too low! guess higher than", guess)

    else:
        print("your guess was too high! guess lower than", guess)

        chances += 1

    if not chances < 5:
        print("you lost! the number was " + number)