import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.agent_position = None
        self.generate_element('P')
        self.generate_element('W')
        self.generate_element('G')

    def generate_element(self, symbol):
        position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        while self.grid[position[0]][position[1]] != '':
            position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.grid[position[0]][position[1]] = symbol

    def display_world(self):
        for row in self.grid:
            print(" ".join(row))
        print()

# Example usage
wumpus_world = WumpusWorld(5)
wumpus_world.display_world()
