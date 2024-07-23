import tkinter as tk

# Create an ui for the application in stonevale/app.py

def display_ui():
    # Create the main window
    window = tk.Tk()
    window.title("Stonevale")

    # Create the labels and entry fields for player moves
    player1_label = tk.Label(window, text="Player 1, please enter your move (rock, paper, or scissors):")
    player1_label.pack()
    player1_entry = tk.Entry(window)
    player1_entry.pack()

    player2_label = tk.Label(window, text="Player 2, please enter your move (rock, paper, or scissors):")
    player2_label.pack()
    player2_entry = tk.Entry(window)
    player2_entry.pack()

    # Create the button to determine the winner
    button = tk.Button(window, text="Determine Winner", command=lambda: determine_winner(player1_entry.get(), player2_entry.get()))
    button.pack()

    # Create the label to display the result
    result_label = tk.Label(window, text="Result:")
    result_label.pack()
    result_text = tk.StringVar()
    result_display = tk.Label(window, textvariable=result_text)
    result_display.pack()

    def determine_winner(move1, move2):
        if move1 == move2:
            result_text.set("It's a tie!")
        elif move1 == "rock":
            if move2 == "scissors":
                result_text.set("Player 1 wins!")
            else:
                result_text.set("Player 2 wins!")
        elif move1 == "paper":
            if move2 == "rock":
                result_text.set("Player 1 wins!")
            else:
                result_text.set("Player 2 wins!")
        elif move1 == "scissors":
            if move2 == "paper":
                result_text.set("Player 1 wins!")
            else:
                result_text.set("Player 2 wins!")
        else:
            result_text.set("Invalid move! Please enter rock, paper, or scissors.")

    # Run the main event loop
    window.mainloop()

display_ui()