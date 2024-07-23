import unittest
from app import Creature, print_board, battle

class TestGridlockArena(unittest.TestCase):

    def setUp(self):
        self.dragon = Creature("Dragon", (2, 2), ["RIGHT", "LEFT", "DOWN"], 7, "🐉")
        self.goblin = Creature("Goblin", (2, 3), ["LEFT", "RIGHT", "UP"], 3, "👺")
        self.ogre = Creature("Ogre", (0, 0), ["RIGHT", "DOWN", "DOWN"], 5, "👹")
        self.creatures = [self.dragon, self.goblin, self.ogre]

    def test_creature_initialization(self):
        self.assertEqual(self.dragon.name, "Dragon")
        self.assertEqual(self.dragon.position, (2, 2))
        self.assertEqual(self.dragon.moves, ["RIGHT", "LEFT", "DOWN"])
        self.assertEqual(self.dragon.power, 7)
        self.assertEqual(self.dragon.icon, "🐉")

    def test_creature_movement(self):
        self.dragon.move()
        self.assertEqual(self.dragon.position, (2, 3))
        self.goblin.move()
        self.assertEqual(self.goblin.position, (2, 2))

    def test_battle_mechanics(self):
        # Move Dragon to (2, 3)
        self.dragon.position = (2, 3)
        # Move Goblin to (2, 2), then Dragon back to (2, 2) causing a battle
        self.goblin.position = (2, 2)
        self.dragon.position = (2, 2)
        battle(self.creatures)
        # Check if at least one of the creatures' score has been updated
        self.assertTrue(self.dragon.score > 0 or self.goblin.score > 0)

    def test_board_visualization(self):
        # This test would require capturing stdout to verify the board's printout, which is complex and not shown here.
        pass

    def test_end_of_battle(self):
        for creature in self.creatures:
            while creature.moves:
                creature.move()
        battle(self.creatures)
        self.assertTrue(all(not creature.moves for creature in self.creatures))

class TestBattleFunction(unittest.TestCase):
    def test_battle(self):
        # Create creatures with positions that will result in a battle
        dragon = Creature("Dragon", (2, 2), [], 7, "🐉")
        goblin = Creature("Goblin", (2, 2), [], 3, "👺")
        # Ogre is added to ensure it does not interfere with the battle
        ogre = Creature("Ogre", (0, 0), [], 5, "👹")

        creatures = [dragon, goblin, ogre]
        battle(creatures)  # This should update the scores based on the battle

        # Check if the scores are as expected
        # Dragon should have 7 - 3 = 4 points, Goblin should have 3 - 7 = -4 points, Ogre remains unaffected
        self.assertEqual(dragon.score, 4, "Dragon's score should be 4 after the battle")
        self.assertEqual(goblin.score, -4, "Goblin's score should be -4 after the battle")
        self.assertEqual(ogre.score, 0, "Ogre's score should remain 0 as it was not part of the battle")


if __name__ == '__main__':
    unittest.main()