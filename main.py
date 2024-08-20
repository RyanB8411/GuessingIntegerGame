#Ryan B
###Guessing game where we will have to select two numbers and
#the program will adapt a range and user will have to select
#the random number that is generated

# import random
# start_range = int(input("\nPlease enter an integer for the starting range of your guessing game.\t"))
# end_range = int(input("\nPlease enter an integer for the ending range of your guessing game.\t"))

# random_num = random.randrange(start_range, end_range)
# print(random_num)
# while True:
#     guess = int(input(f"Please guess the random number from {start_range} to {end_range}. \t"))
#     if guess == random_num:
#         print(f"\n\nYou guessed it, it was {random_num}. I hope you have a great day!!!")
#         break
#     else:
#         print(f"\n{guess} is not it. Try again!")
displace_input = float(.2)

reciprocal_val = 1/displace_input

print(f'The reciprocal of displacement = 1 / {displace_input:.3f} = {reciprocal_val:.3f}')

cube_edge = float(3.4)
cube_volume = cube_edge * cube_edge * cube_edge

print(f'(\'Volume is\') , {cube_volume:.5f}')

num1 = float(10)
num2 = float(14)

mean_of_two = (num1+num2) / 2

print(f'Mean is {mean_of_two:.3f}')