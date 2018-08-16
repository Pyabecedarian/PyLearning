"""
Rolling two dice, analyze the distribution
of the results
"""
import pygal
from generating_data.Dice import Die
# Create two D6 Dice
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist._title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_dice_visual.svg')
