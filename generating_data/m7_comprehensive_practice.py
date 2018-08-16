"""
Using both matplotlib and Pygal to make a rolling-2x D6-visualization
"""

import matplotlib.pyplot as plt
import pygal
from generating_data.Dice import Die

# Create two D6
die_1 = Die()
die_2 = Die()

# Rolling the dice 5000 times, store the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the frequencies of the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
x_label_list = [i for i in range(2, max_result+1)]
x_label_str = []
for value in x_label_list[:]:
    frequency = results.count(value)
    frequencies.append(frequency)
    sub_str = str(value)
    x_label_str.append(sub_str)


# Visualize the results using pygal
hist = pygal.Bar()
hist._title = "Results of rolling two D6"
hist.x_labels = x_label_str
hist._x_title = "Results"
hist._y_title = "Frequency"
hist.add("D6 + D6", frequencies)
hist.render_to_file("two_dice_visual_1.svg")

# visualize the results using matplotlib
plt.plot(x_label_list, frequencies, linewidth=5)
plt.show()
