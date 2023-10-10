from art import logo, vs
import random 
from game_data import data

past_profiles = []

def generate_next_choice(data):
    return random.choice(data)

def generate_unique_profile(data):
    while True:
            profileB = generate_next_choice(data)
            if profileB['name'] not in past_profiles:
                past_profiles.append(profileB['name'])
                break
    return profileB

def get_player_decision(profileA, profileB):
    while True:
            decision = input(f"Who has more followers? Type 'A' or 'B': ").lower()
            if decision == 'a':
                player_answer = profileA
                break
            elif decision == 'b':
                player_answer = profileB
                break
            else:
                print("Please input 'A' or 'B'. ")
    return player_answer

def display_profiles(profileA, profileB):
      print(f"Compare A: {profileA['name']}, a {profileA['description']}, from {profileA['country']}")
      print(vs)
      print("\n")
      print(f"Against B: {profileB['name']}, a {profileB['description']}, from {profileB['country']}")

def check_answer(player_answer, solution, score, profileB):
     if player_answer != solution:
         print(f"\nCorrect answer was {solution['name']} with {solution['follower_count']} million followers.\n\nYou lose, you got {score} correct answers in total")
         return score, None
     else:
         score+=1
         if len(past_profiles) == len(data):
             print(f"You win the game with a maximum score of {score}")
             return score, None
         else:
             print(logo)
             print("You're right")
             print(f"Current score: {score}")
             return score, profileB

def game():
    score = 0
    profileA = generate_next_choice(data)
    past_profiles.append(profileA['name'])
    while True:
        profileB = generate_unique_profile(data)
        display_profiles(profileA, profileB)
        
        solution = profileA if profileA['follower_count'] > profileB['follower_count'] else profileB
        player_answer = get_player_decision(profileA, profileB)

        score, new_profileA = check_answer(player_answer, solution, score, profileB)
        if new_profileA:  
            profileA = new_profileA
        else:
            break


while True:
    print(logo)
    past_profiles.clear()
    game()
    if input("Do you want to play again? 'yes' to play again, 'no' exit. ").lower() == 'no':
        print("Thanks for playing!\nbye!")
        break
    print("\n")