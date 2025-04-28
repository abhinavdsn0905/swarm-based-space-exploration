import numpy as np
import random

class Robot:
    def __init__(self, idx, exploration_map, grid_size):
        while True:
            x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if exploration_map[x, y] == 0:
                break
        self.idx = idx
        self.pos = np.array([x, y])
        self.path = [tuple(self.pos)]
        self.grid_size = grid_size
        self.exploration_map = exploration_map

    def move(self):
        directions = [np.array(d) for d in [
            [0, 1], [1, 0], [0, -1], [-1, 0],
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ]]
        random.shuffle(directions)
        for d in directions:
            new_pos = self.pos + d
            if 0 <= new_pos[0] < self.grid_size and 0 <= new_pos[1] < self.grid_size:
                if self.exploration_map[new_pos[0], new_pos[1]] != -1:
                    self.pos = new_pos
                    self.path.append(tuple(self.pos))
                    return

    def sense_and_update_map(self):
        x, y = self.pos
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    if self.exploration_map[nx, ny] == 0:
                        self.exploration_map[nx, ny] = 1