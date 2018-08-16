"""Creating the Die Class, Roll the die, and analyse the results"""
import pygal
from generating_data.Dice import Die


"""Rolling the Die"""
# Create a D6
die = Die()
# Make some roll, and store the results in a list
results = []
for _ in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# Making a Histogram
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
