import math
import numpy as np

r= 9
print(math.pi * r**2)

# Travel distance of Moon over 12 degrees. Store in dist.
r= 192500
print(r * math.radians(12))

baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(type(np_baseball))

np_baseball_4 = np_baseball * 4
print(np_baseball_4)

print(np_baseball[2])

lower = np_baseball < 195
print (lower)
print(np_baseball[lower])

#2d arrays
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)
#print out the third row
print(np_baseball[2,:])
#print out the second column
print(np_baseball[:,1])
#print out second row first column
print(np_baseball[1,0])
np_baseball_1 = np_baseball * 2
print(np_baseball_1)
np_baseball_2 = np_baseball + np.array([20,20])
print(np_baseball_2)
np_baseball_3 = np_baseball + np_baseball
print(np_baseball_3)

np_row1 = np_baseball[:,0]
#mean and median and corrcoef
print(np.mean(np_row1))
print(np.median(np_row1))
print(np.corrcoef(np_baseball[:,0], np_baseball[:,1]))

print("===========================================================================================")
#challenge
positions = ['gk', 'm', 'd', 'a', 'a', 'gk', 'md', 'a', 'd', 'm', 'gk','a', 'a', 'gk', 'm']
heights = [123, 234, 34, 56, 23, 23, 45, 789, 567, 234, 123, 235, 123, 45, 78]

np_positions = np.array(positions)
np_heights = np.array(heights)

gk_heights = np_heights[np_positions == 'gk']
other_heights = np_heights[np_positions != 'gk']

print(gk_heights)
print(other_heights)

