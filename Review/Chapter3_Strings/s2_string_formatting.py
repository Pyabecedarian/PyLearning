"""
1>  Conversion Specifiers (percent sign):
            %d, %s, %f

2>  Template strings:
            from string import Template

3>  Format string:
            "{} or {name}".format(value)
"""

# TODO  1. conversion specifier: %
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values, end='\n\n')


# TODO  2. template strings: syntax similar with UNIX shells
from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
formatted_tmpl = tmpl.substitute(who="Mars", what="Dusty")
print(formatted_tmpl, end='\n\n')


# TODO  3. format string: {} or {name}

# 3.1  fields have no name or an index
format_str = "{}, {} and {}".format('first', 'second', 'third')
print(format_str)
format_str = "{0}, {1} and {2}".format('first', 'second', 'third')
print(format_str)

# 3.2 fields with names
PI = 3.1415926
format_str = "{name} is approximately {value:.2f}.".format(value=PI, name='pi')
print(format_str)

# 3.2.1 Shortcut in python 3.6: If variables named identically to field name
from math import e
format_str = f"Euler's constant is roughly {e:.3f}."
print(format_str)
