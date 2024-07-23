# python application
# Create a basic CLI application that accepts text input and returns a response.
# There are two players: Rok and Papyra
# The players are asked for their input one after another


# Import necessary libraries
import sys

# Validate player input
def validate_input(player_input):
    valid_inputs = ["rock", "paper", "scissors"]
    if player_input.lower() in valid_inputs:
        return True
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        return False

# Adjusted determine_winner function to return winning choice
def determine_winner(player1_choice, player2_choice):
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if player1_choice == player2_choice:
        return "It's a tie!", None
    elif rules[player1_choice] == player2_choice:
        return "Player 1 wins!", player1_choice
    else:
        return "Player 2 wins!", player2_choice

# Modified main function to include 5 rounds of duels
def main():
    print("Welcome to the CLI application!")
    
    players = ["Rok", "Papyra"]
    scores = {"Rok": 0, "Papyra": 0}
    
    for round in range(1, 6):  # 5 rounds
        print(f"\nRound {round}")
        choices = []
        
        for player in players:
            while True:  # Keep asking for input until valid
                print(f"{player}, it's your turn.")
                player_input = input("Please enter rock, paper, or scissors: ")
                if validate_input(player_input):
                    print(f"{player} entered: {player_input}")
                    choices.append(player_input)
                    break  # Exit the loop if input is valid
        
        # Adjust the scoring part in the main loop
        # Assuming the rest of the code remains the same
        result, winning_choice = determine_winner(choices[0], choices[1])
        print(result)
        if winning_choice:
            points = {"rock": 1, "paper": 2, "scissors": 3}
            if "Player 1" in result:
                scores["Rok"] += points[winning_choice]
            elif "Player 2" in result:
                scores["Papyra"] += points[winning_choice]
        
    # Announce the overall winner
    print(f"\nFinal Scores: {scores}")
    if scores["Rok"] > scores["Papyra"]:
        print("Rok is the overall winner!")
    elif scores["Rok"] < scores["Papyra"]:
        print("Papyra is the overall winner!")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()