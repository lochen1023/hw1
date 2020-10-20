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

def drawEnvironment( ax, env ):
  height, width, obstacles, rewards = env
  ax.set_axis_off()
  ax.set_ylim( -0.5, height + 1 )
  ax.set_xlim( -0.5, width + 1 )

  for y in range(0,height):
    ax.text(-0.5, y + 0.3, chr( (ord('A') + y ) ), fontsize=12 )

  for x in range(0,width):
    ax.text(x + 0.4, height + 0.3, str(x), fontsize=12 )

  for y in range(0,height):
    for x in range(0,width):
      bg = mpatches.Rectangle( (x,y), 1.0, 1.0, linewidth=2, color="white", fill=True )
      r = mpatches.Rectangle( (x,y), 1.0, 1.0, linewidth=2, color="black", fill=False )
      ax.add_patch(bg)
      ax.add_patch(r)

  for oy, ox in obstacles:
    bg = mpatches.Rectangle( (ox,oy), 1.0, 1.0, linewidth=2, color="#2020a0", fill=True )
    r = mpatches.Rectangle( (x,y), 1.0, 1.0, linewidth=2, color="black", fill=False )
    ax.add_patch(bg)
    ax.add_patch(r)
    
  for rc, r in rewards:
    ry,rx = rc
    if r > 0:
      col = '#c02020'
    elif r < 0:
      col = '#20c020'
    else:
      col = '#ffffff'

    bg = mpatches.Rectangle( (rx,ry), 1.0, 1.0, linewidth=2, color=col, fill=True )
    rect = mpatches.Rectangle( (rx,ry), 1.0, 1.0, linewidth=2, color="black", fill=False )
    ax.add_patch(bg)
    ax.add_patch(rect)
    ax.text(rx+0.2, ry + 0.3, str(r), fontsize=12)
