import numpy as np
import random

class Brain:
    def __init__(self, maze):
        self.maze = maze
        self.belief = np.zeros(maze.maze.shape)
        self.informationCache = []

    def accept_information(self, observation):
        self.informationCache.append(observation)
        return True

    def determine_direction(self):
        return random.choice(["left", "right", "up", "down"])
