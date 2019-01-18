# Just to see what the Standard Python Module consists of
# Python with builtin modules is well equipped
# when any module is imported it adds it into dir list

#### Most Important - python does not have access specifiers concept so everything in python is
#       accessible from anywhere, however, giving "__" at the begining and to the end specifies
#       it as a keyword.

# some of the modules in python are written in C language

import shelve   # CTRL click on it shows the source code if written in python

print(dir())

print(dir(__doc__))

print(dir(shelve))

#help(shelve)    # opens help content on shelve
