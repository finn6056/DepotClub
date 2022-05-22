import random

print("Welcome to Paper, Scissors, Rock")


user_input = input("Enter a choice (Rock, Paper, Scissors):   ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")
