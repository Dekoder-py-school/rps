import random

user_score = 0
cpu_score = 0

while user_score <= 10 and cpu_score <= 10:
    user_choice = input('Choose rock, paper or scissors: ')
    cpu_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == "rock" and cpu_choice == "scissors":
        user_score += 1