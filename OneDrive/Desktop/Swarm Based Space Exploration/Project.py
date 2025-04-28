# Enter your code here
import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
GRID_SIZE = 50
NUM_ROBOTS = 5
STEPS = 200

# Create map: 0 = unexplored, 1 = explored, -1 = obstacle
exploration_map = np.zeros((GRID_SIZE, GRID_SIZE))

# Add random obstacles
for _ in range(int(GRID_SIZE * GRID_SIZE * 0.1)):  # 10% obstacles
    x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    exploration_map[x, y] = -1

# Robot class
class Robot:
    def __init__(self, idx):
        while True:
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if exploration_map[x, y] == 0:
                break
        self.idx = idx
        self.pos = np.array([x, y])
        self.path = [tuple(self.pos)]

    def move(self):
        directions = [np.array(d) for d in [
            [0, 1], [1, 0], [0, -1], [-1, 0],
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ]]
        random.shuffle(directions)
        for d in directions:
            new_pos = self.pos + d
            if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE:
                if exploration_map[new_pos[0], new_pos[1]] != -1:
                    self.pos = new_pos
                    self.path.append(tuple(self.pos))
                    return

    def sense_and_update_map(self):
        x, y = self.pos
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if exploration_map[nx, ny] == 0:
                        exploration_map[nx, ny] = 1

# Initialize robots
robots = [Robot(i) for i in range(NUM_ROBOTS)]

# Enable live plot
plt.ion()
fig, ax = plt.subplots(figsize=(7, 7))

# Simulation loop
for step in range(STEPS):
    for robot in robots:
        robot.sense_and_update_map()
        robot.move()

    if step % 5 == 0 or step == STEPS - 1:
        ax.clear()
        ax.imshow(exploration_map, cmap='gray_r')
        for i, robot in enumerate(robots):
            path = np.array(robot.path)
            ax.plot(path[:, 1], path[:, 0], label=f'Robot {i}')
            ax.scatter(path[-1, 1], path[-1, 0], marker='o', s=40)
        ax.set_title(f"Step {step}")
        ax.legend()
        plt.draw()
        plt.pause(0.05)

plt.ioff()

# Show final output
plt.figure(figsize=(7, 7))
plt.imshow(exploration_map, cmap='gray_r')

for i, robot in enumerate(robots):
    path = np.array(robot.path)
    plt.plot(path[:, 1], path[:, 0], label=f'Robot {i}')
    plt.scatter(path[0, 1], path[0, 0], marker='s', color='green', label=f'Start {i}' if i == 0 else "")
    plt.scatter(path[-1, 1], path[-1, 0], marker='o', color='red', label=f'End {i}' if i == 0 else "")

plt.title("Final Map After Exploration")
plt.legend()
plt.grid(False)
plt.show()

# Calculate and print exploration percentage
explored_cells = np.sum(exploration_map == 1)
total_cells = GRID_SIZE ** 2 - np.sum(exploration_map == -1)
coverage = (explored_cells / total_cells) * 100
print(f"\n Final Exploration Coverage: {coverage:.2f}%")
