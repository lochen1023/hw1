import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np
import random

def createRandomEnvironment(height, width, nObstacles, nRewards):
    obstacles = []
    while(len(obstacles) < nObstacles):
        ob = (random.randint(0, height-1), random.randint(0, width-1))
        if ob not in obstacles:
            obstacles.append(ob)

    rewardCoord = []
    reward = []

    while(len(rewardCoord) < nRewards):
        rc = (random.randint(0, height-1), random.randint(0, width-1))
        r = random.randint(-99, 99)
        if (rc not in rewardCoord) and (rc not in obstacles):
            rewardCoord.append(rc)
            reward.append(r)

return (height, width, obstacles, [x for x in zip(rewardCoord, reward)])