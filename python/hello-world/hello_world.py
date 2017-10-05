#
# Skeleton file for the Python "Hello World" exercise.
#

def hello(name=''):
    if (name == '') or (name == None):
        name = "World"
    return "Hello, " + name + "!"
