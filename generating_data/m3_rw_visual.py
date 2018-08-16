"""Plotting the Random Walk"""

import matplotlib.pyplot as plt
from generating_data.m2_random_walk import RandomWalk


# Keep making new walks, as long as the program is active
#
# while True:
#     rw = RandomWalk(50000)
#     rw.fill_walk()
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
#                 cmap=plt.cm.Blues, edgecolors=None, s=1)
#
#     # Emphasize the first and last points
#     plt.scatter(0, 0, c='green', edgecolors=None, s=100)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
#                 edgecolors=None, s=100)
#
#     # Remove the axes
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#
#     # Set the size of plotting window
#     plt.figure(figsize=(10, 6))
#
#     plt.show()
#
#     keep_running = input("Make another walk? ( y / n):  ")
#     if keep_running == 'n':
#         break


"""
Practice:

1>. Molecular Motion: Simulate the path of a pollen grain on the surface of a
drop of water by using plt.plot() instead of plt.scatter(). 
Use default numbers of points 5000.
"""

pollen_grain = RandomWalk()
pollen_grain.fill_walk()

plt.plot(pollen_grain.x_values, pollen_grain.y_values, linewidth=0.5)
plt.scatter(0, 0, c='green', edgecolors=None, s=100)
plt.scatter(pollen_grain.x_values[-1], pollen_grain.y_values[-1],
            c='red', edgecolors=None, s=100)
plt.show()


"""
Practice:

2>. Create a new method called get_step() in which to determine the 
direction and distance for each step

"""
# See "refactor" in m2_random_walk.py
