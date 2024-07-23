# Python
# Encoding: utf-8
#

# Your task is to simulate a battle in the Gridlock Arena. Each creature will make a series of moves, and after each move, the creature might inflict damage on its opponent if they land on the same square. The goal is to accumulate the highest score by the end of the battle. To track the progress of the battle, visualize the grid after each move and display the current scores right below the grid.

# create a 5x5 grid for the arena
# Each cell in the grid can be empty or occupied by a creature.
# Creatures can move up, down, left, or right by one cell.

# Creature Data:
# Name	Start	Moves	Power	Icon
# Dragon	2,2	RIGHT, LEFT, DOWN	7	🐉
# Goblin	2,3	LEFT, RIGHT, UP	3	👺
# Ogre	0,0	RIGHT, DOWN, DOWN	5	👹

# Battle Dynamics:
# Creatures take turns making moves.
# If two creatures land on the same cell after a move, they both inflict damage on each other.
# Points are awarded based on the damage inflicted.
# The battle ends when all moves are completed.


# Output:
# After each move, visualize the grid by printing it to the console using ⬜️ to represent a cell.
# Above the grid add a title that either says "Initial Board" (to show the initial state of the board) or "Move X" where X is the current move number.
# Use each creature's icon to represent it on the grid.
# Empty cells can be represented by a ⬜️.
# Battle cells can be represented by a 🤺.
# Display the current scores for each creature right below the grid after each move.
# At the end of the battle, return the total points each creature accumulated.

class Creature:
    def __init__(self, name, start, moves, power, icon):
        self.name = name
        self.position = start
        self.moves = moves
        self.power = power
        self.icon = icon
        self.score = 0

    def move(self):
        if self.moves:
            direction = self.moves.pop(0)
            if direction == "RIGHT":
                self.position = (self.position[0], self.position[1] + 1)
            elif direction == "LEFT":
                self.position = (self.position[0], self.position[1] - 1)
            elif direction == "UP":
                self.position = (self.position[0] - 1, self.position[1])
            elif direction == "DOWN":
                self.position = (self.position[0] + 1, self.position[1])

def print_board(creatures, move_number=None):
    grid_size = 5  # Assuming a 5x5 grid
    grid = [["⬜️" for _ in range(grid_size)] for _ in range(grid_size)]
    for creature in creatures:
        if grid[creature.position[0]][creature.position[1]] == "⬜️":
            grid[creature.position[0]][creature.position[1]] = creature.icon
        else:
            grid[creature.position[0]][creature.position[1]] = "🤺"
    title = "Initial Board" if move_number is None else f"Move {move_number}"
    print(title)
    for row in grid:
        print(" ".join(row))
    for creature in creatures:
        print(f"{creature.name}: {creature.score}")

def battle(creatures):
    positions = {}
    for creature in creatures:
        if creature.position in positions:
            positions[creature.position].append(creature)
        else:
            positions[creature.position] = [creature]
    for pos, contenders in positions.items():
        if len(contenders) > 1:
            for creature in contenders:
                creature.score = creature.power - sum([opponent.power for opponent in contenders if opponent != creature])

creatures = [
    Creature("Dragon", (2, 2), ["RIGHT", "LEFT", "DOWN"], 7, "🐉"),
    Creature("Goblin", (2, 3), ["LEFT", "RIGHT", "UP"], 3, "👺"),
    Creature("Ogre", (0, 0), ["RIGHT", "DOWN", "DOWN"], 5, "👹")
]

print_board(creatures)
move_number = 1
while any(creature.moves for creature in creatures):
    for creature in creatures:
        creature.move()
        battle(creatures)
    print_board(creatures, move_number)
    move_number += 1
