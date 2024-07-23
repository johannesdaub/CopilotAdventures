# Test app.py

# Test the CLI application running in app.py with the following inputs:
# Moves for Rok (Player 1)
# Round 1	Round 2	Round 3	Round 4	Round 5
# scissors	paper	scissors	rock	rock
#
# Moves for Paprya (Player 2)
# Round 1	Round 2	Round 3	Round 4	Round 5
# rock	rock	paper	scissors	paper

# Winner will be:
# Round 1: Paprya 
# Round 2: Rok
# Round 3: Rok
# Round 4: Rok
# Round 5: Paprya

import unittest
from unittest.mock import patch
from io import StringIO
import app  # Import the module that contains the game logic

class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'scissors',  # Rok Round 1
        'rock',      # Papyra Round 1
        'paper',     # Rok Round 2
        'rock',      # Papyra Round 2
        'scissors',  # Rok Round 3
        'paper',     # Papyra Round 3
        'rock',      # Rok Round 4
        'scissors',  # Papyra Round 4
        'rock',      # Rok Round 5
        'paper'      # Papyra Round 5
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_logic(self, mock_stdout, mock_input):
        app.main()  # Run the main function of the game
        output = mock_stdout.getvalue()

        # Assertions for each round's winner
        self.assertIn("Player 2 wins!", output)  # Assuming Papyra is Player 2 in Round 1
        self.assertIn("Player 1 wins!", output)  # Assuming Rok is Player 1 in Round 2, 3, and 4
        self.assertIn("Player 2 wins!", output)  # Assuming Papyra is Player 2 in Round 5

        # Since the output will contain all rounds together, these checks are basic.
        # For more precise checks, you would need to analyze the output more granularly
        # to ensure the wins align with the correct rounds.

if __name__ == '__main__':
    unittest.main()