#Ryan B
##Guessing game where we will have to select two numbers and
#the program will adapt a range and user will have to select
#the random number that is generated

import random
start_range = int(input("\nPlease enter an integer for the starting range of your guessing game.\t"))
end_range = int(input("\nPlease enter an integer for the ending range of your guessing game.\t"))

random_num = random.randrange(start_range, end_range)
print(random_num)
while True:
    guess = int(input(f"Please guess the random number from {start_range} to {end_range}. \t"))
    if guess == random_num:
        print(f"\n\nYou guessed it, it was {random_num}. I hope you have a great day!!!")
        break
    else:
        print(f"\n{guess} is not it. Try again!")
