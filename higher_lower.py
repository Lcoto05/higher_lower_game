from higher_lower_art import logo, vs
from higher_lower_data import data
import random

def pick_celebrity():
    return random.choice(data)
    
def format(celebrity):
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
    return f"{name}, a {description}, from {country}."

def check_guess(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def higher_lower():
    print(logo)
    score = 0
    continue_game = True
    celebrity_a = pick_celebrity()
    celebrity_b = pick_celebrity()

    while continue_game:
        celebrity_a = celebrity_b
        celebrity_b = pick_celebrity()
        while celebrity_a == celebrity_b:
            celebrity_b = pick_celebrity()

        print(f"Compare A: {format(celebrity_a)}.")
        print(vs)
        print(f"Against B: {format(celebrity_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = celebrity_a["follower_count"]
        b_follower_count = celebrity_b["follower_count"]
        is_correct = check_guess(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"Correct! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}.")

higher_lower()



