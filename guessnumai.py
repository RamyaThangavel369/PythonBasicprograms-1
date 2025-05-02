import random
print("My Guessing number between 1 and 10")

secret_number=random.randint(1,10)#AI PICKS A RANDOM NUMBER
while True:
    guess = int(input("Guessing number:"))

    if guess<secret_number:
        print("Too low! Try it again")
    elif guess>secret_number:
        print("Too High!Try it again")
    else:
        print("You got it!Great job")
        break