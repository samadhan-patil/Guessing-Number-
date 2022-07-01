from pickle import TRUE
import random

MIN_LIMIT = 1
MAX_LIMIT = 100
actual_number =random.randint(MIN_LIMIT,MAX_LIMIT)
attempts =5

print("This is an amazing guessing number game.")
print("In which you have 5 attempts to guess the correct number between 1 to 100.")
print("if you guess the correct number you will the game.")
for i in range (attempts):
   guess = int(input("Guess The Number :"))
   if guess == actual_number :
    print("You guessed correct number in ",i-1,"attempts.") 
    print("Thanks for playing!")
      
   elif guess <actual_number :
    print("Your guess is too low ")
   else :
    print("Your guess is too high.")
print("You lose the game, the original number was", actual_number,", better luck next time!")
print("Thanks for playing!")
    


       
    

