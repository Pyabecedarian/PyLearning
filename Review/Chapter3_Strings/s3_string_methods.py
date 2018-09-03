"""
1>  .center():
        Center the string by padding it on either side with a given fill
        character --- spaces by default

    APPENDIX: .rfind(),  .index(),  .rindex(),  .count(),  .startswith()
              .endswith()


2>  .find()
        find a substring within a larger string.
        Return the leftmost index where the substring is found,
        or if it's not found, return -1

    APPENDIX: .rfind(),  .index(),  .rindex(),  .count(),  .startswith()
              .endswith()


3>  .join()
        Join the elements of a sequence, it's the inverse of .split()

    APPENDIX: .split()


4>  .lower()
        Returns a lowercase version of the string

    APPENDIX: .islower(),  .istitle(),  .isupper(),  .translate()
              .capitalize(),  .casefold(),  .swapcase(),  .title()
              .upper()


5>  .replace()
        Returns a string where all the occurrences of one string have
        been replaces by another

    APPENDIX: .translate(),  .expandtabs()


6>  .split()
        The inverse of .join() and is used to split a string into a sequence

    APPENDIX: .partition(),  .rpartition(),  .rsplit(),  .rsplitlines()


7>  .strip()
        Return a string where whitespace on the left and right
        (not internally) has been removed .

    APPENDIX: .lstrip(),  .rstrip()


8>  .translate()
        Similar to .replace() except translate works only with single
        characters.
        Before using translate(), use .maketrans() to make a
        translation table.


9>  .isalnum(),  .isalpha(),  .isdecimal(),  .isdigit(),  .isidentifier(),
    .islower(),  .isnumeric(),  .isprintable(),  isspace(),  .istitle(),
    .isupper()

"""


# TODO  1. center()
a_str = 'The Middle by Jimmy Eat World'
print(a_str.center(39))
print(a_str.center(39, '*'), end='\n\n')


# TODO  2. find()
a_str = 'With a moo-moo here, and a moo-moo there'
print(a_str.find('moo'), end='\n\n')


# TODO  3. join()
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs), end='\n\n')
# NOTE: All the sequence elements to be joined must all be strings!


# TODO  4. lower()
a_str = 'Trondheim Hammer Dance'
print(a_str.lower(), end='\n\n')


# TODO  5. replace()
a_str = 'This is a test'
print(a_str.replace('is', 'eez'), end='\n\n')


# TODO  6. split()
a_str = '1+2+3+4+5'
print(a_str.split('+'))
dirs = '/usr/bin/env'
print(dirs.split('/'))
def_str = 'Using  the  default'
print(def_str.split(), end='\n\n')


# TODO  7. strip()
strip_str = '    internal whitespace is kept     '
print(strip_str.strip())
strip_str = '**** SPAM * for * everyone!!! ***'
print(strip_str.strip(' *!'), end='\n\n')


# TODO  8. translate()
table = str.maketrans('cs', 'kz')
table1 = str.maketrans('cs', 'kz', ' ')
a_str = 'this is an incredible test'
print(a_str)
print(a_str.translate(table))
print(a_str.translate(table1), end='\n\n')


# TODO  9. Is My String...
"""
Plenty of string methods that start with is, that determine whether
your string has certain properties, in which case the methods return
True or False.
"""