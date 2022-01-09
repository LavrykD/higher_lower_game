import art
import game_data
import random

def generation():
  """Generate the random choice of star from the game_data list."""
  rnd_choice = random.choice(game_data.data)
  return rnd_choice

def lose():
  global SCORE
  print(art.logo)
  print(f"Sorry, you're wrong. Final score: {SCORE}.")

SCORE = 0
end_of_game = False
choice_A = generation()
choice_B = generation()

while not end_of_game:
  print(art.logo)

  if SCORE >= 1:
    print(f"You're right! Your score is {SCORE}.")
    
  print(f"Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}.")

  print(art.vs)

  while choice_A == choice_B:
    choice_B = generation()
    
  print(f"Compare B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}.")

  answer = input("Who has more followers? Type 'A' or 'B': ")

  if answer == "A":
    if choice_A['follower_count'] > choice_B['follower_count']:
      SCORE += 1
      choice_A = choice_A
      choice_B = generation()
    else:
      lose()
      end_of_game = True
  elif answer == "B":
    if choice_B['follower_count'] > choice_A['follower_count']:
      SCORE += 1
      choice_A = choice_B
      choice_B = generation()
    else:
      lose()
      end_of_game = True
