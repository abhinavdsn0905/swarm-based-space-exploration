import numpy as np
import random
import matplotlib.pyplot as plt

def generate_map(grid_size, obstacle_ratio=0.1):
    exploration_map = np.zeros((grid_size, grid_size))
    num_obstacles = int(grid_size * grid_size * obstacle_ratio)
    for _ in range(num_obstacles):
        x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        exploration_map[x, y] = -1
    return exploration_map

def plot_map(ax, exploration_map, robots, step=None, show_paths=True):
    ax.clear()
    ax.imshow(exploration_map, cmap='gray_r')
    for i, robot in enumerate(robots):
        path = np.array(robot.path)
        if show_paths:
            ax.plot(path[:, 1], path[:, 0], label=f'Robot {i}')
        ax.scatter(path[-1, 1], path[-1, 0], marker='o', s=40)
    if step is not None:
        ax.set_title(f"Step {step}")
    ax.legend()
    plt.draw()
    plt.pause(0.05)

def plot_final_map(exploration_map, robots):
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

def calculate_coverage(exploration_map):
    explored_cells = np.sum(exploration_map == 1)
    total_cells = exploration_map.size - np.sum(exploration_map == -1)
    coverage = (explored_cells / total_cells) * 100
    return coverage