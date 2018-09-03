"""
database = {}
database['first'] = {first_name:[full_name]}
database['middle'] = {middle_name:[full_name]}
database['last'] = {last_name:[last_name]}
"""


def init(database):
    """initiate a database"""
    database['first'] = {}
    database['middle'] = {}
    database['last'] = {}


def lookup(data, label, name):
    """return the name"""
    return data[label].get(name)


def store(data, full_name):
    """store info"""
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames = {}
init(MyNames)
store(MyNames, 'Chris LIU')
print(lookup(MyNames, 'first', 'Chris'))