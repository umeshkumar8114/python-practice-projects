import random

# Choices and win conditions
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
rules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

# Descriptive actions for each win interaction
actions = {
    ('scissors', 'paper'): 'cuts',
    ('paper', 'rock'): 'covers',
    ('rock', 'lizard'): 'crushes',
    ('lizard', 'spock'): 'poisons',
    ('spock', 'scissors'): 'smashes',
    ('scissors', 'lizard'): 'decapitates',
    ('lizard', 'paper'): 'eats',
    ('paper', 'spock'): 'disproves',
    ('spock', 'rock'): 'vaporizes',
    ('rock', 'scissors'): 'crushes'
}

# Game statistics
num_games = 0
user_wins = 0
computer_wins = 0
games_tied = 0

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

while True:
    user_input = input("Enter your choice: ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Please enter rock, paper, scissors, lizard, or spock: ").lower()

    computer_choice = random.choice(choices)
    print(f"Computer chooses: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
        games_tied += 1
    elif computer_choice in rules[user_input]:
        action = actions.get((user_input, computer_choice), "defeats")
        print(f"{user_input.title()} {action} {computer_choice.title()} — You win!")
        user_wins += 1
    else:
        action = actions.get((computer_choice, user_input), "defeats")
        print(f"{computer_choice.title()} {action} {user_input.title()} — Computer wins!")
        computer_wins += 1

    num_games += 1

    play_again = input("Play again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        play_again = input("Please enter 'yes' or 'no': ").lower()
    if play_again == 'no':
        break

# Game summary
print("\nGame Summary:")
print(f"Total games played: {num_games}")
print(f"Games you won: {user_wins}")
print(f"Games the computer won: {computer_wins}")
print(f"Tied games: {games_tied}")