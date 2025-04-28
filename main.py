import numpy as np
import matplotlib.pyplot as plt
from robot import Robot
from utils import generate_map, plot_map, plot_final_map, calculate_coverage

# Parameters
grid_size = 50
num_robots = 5
steps = 200
obstacle_ratio = 0.1

# Create map
exploration_map = generate_map(grid_size, obstacle_ratio)

# Initialize robots
robots = [Robot(i, exploration_map, grid_size) for i in range(num_robots)]

# Enable live plot
plt.ion()
fig, ax = plt.subplots(figsize=(7, 7))

# Simulation loop
for step in range(steps):
    for robot in robots:
        robot.sense_and_update_map()
        robot.move()
    if step % 5 == 0 or step == steps - 1:
        plot_map(ax, exploration_map, robots, step)

plt.ioff()

# Show final output
plot_final_map(exploration_map, robots)

# Calculate and print exploration percentage
coverage = calculate_coverage(exploration_map)
print(f"\nFinal Exploration Coverage: {coverage:.2f}%")