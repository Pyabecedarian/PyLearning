import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
#
# plt.plot(squares, linewidth=5)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Values", fontsize=14)
#
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()


"""Correcting the Plot"""

# input_values = [1, 2, 3, 4, 5]
# plt.plot(input_values, squares, linewidth=5)
# plt.show()

# rect_x = [0, 1, 1, 0, 0]
# rect_y = [0, 0, 1, 1, 0]
#
# tria_x = [0, 2, 1, 0]
# tria_y = [0, 0, 1, 0]
#
# # plt.plot(rect_x, rect_y)
# plt.plot(tria_x,tria_y)
# plt.show()

"""Plotting and Styling Individual Points with Scatter()"""
""" Scatter() plot one point"""

# points = [2, 4]
# plt.scatter(*points, s=200)
# plt.xlabel("Square Numbers", fontsize=14)
# plt.ylabel("Value", fontsize=14)
#
# plt.tick_params(axis='both', which='major', labelsize=10)
#
# plt.show()

"""Plotting a Series of Points with Scatter()"""
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
#             edgecolors=None, s=40)
# plt.xlabel("Square Numbers", fontsize=14)
# plt.ylabel("Value", fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=10)
#
# # Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])
#
# # plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')


"""
TEST:   PLOT THE 1ST 5000 NUMBERS OF CUBES AND USE COLORMAP
"""
#
# x_values = list(range(1, 5001))
# y_values = [x ** 3 for x in x_values]

# plt.plot(x_values, y_values, linewidth=5)
# plt.xlabel("Cube Numbers", fontsize=14)
# plt.ylabel("Values", fontsize=14)
#
# plt.show()

# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors=None, s=10)
#
# plt.show()
