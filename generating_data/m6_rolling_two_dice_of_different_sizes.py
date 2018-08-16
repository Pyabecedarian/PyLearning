"""
Rolling two dice, one is D6, another is D10, analyze the distribution of
the results
"""

import pygal
from generating_data.Dice import Die

# Create two Dice: D6 & D10
die_1 = Die()
die_2 = Die(10)

# Rolling two dice 5000 times, and store the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
x_label_list = list(range(2, max_result+1))
for value in x_label_list:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

# Create x_label
for x_label in x_label_list[:]:
    index = x_label_list[:].index(x_label)
    x_label_list[index] = str(x_label)

hist.title = "Results of rolling a D6 and D10"
hist.x_labels = x_label_list
hist._x_title = "Results"
hist._y_title = "Frequency"
hist.add("D6 + D10", frequencies)
hist.render_to_file('sum_of_D6_and_D10.svg')
