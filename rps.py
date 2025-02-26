import random

user_score = 0
cpu_score = 0

user_choice = input('Choose rock, paper or scissors: ').lower()
cpu_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == "rock" and cpu_choice == "scissors":
    user_score += 1