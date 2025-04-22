""" Guessing_game():
   secret_number=5
   guess=int(input("Guessing number between 1 to 10:"))
   if guess==secret_number:
       print("wow your guessed is right!")
   else:
        print("Try it again!")
Guessing_game()"""
#WHILE LOOP GUESSING GAME
def Guessing_game():
    secret_number=7
    guess=0
   while guess != secret_number:
         guess=int(input("Guessing number between 1 to 10:"))
         if guess<secret_number:
            print("Too Low!")
         elif guess>secret_number:
            print("Too High!")
         else:
            print("Try again!")
Guessing_game()