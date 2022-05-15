import random
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_input = input("Please press any key to generate a random letter\n")
random_output = random.choice(alphabet)

print("Here is the random letter ", random_output)