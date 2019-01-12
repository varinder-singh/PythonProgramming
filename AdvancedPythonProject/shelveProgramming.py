# shelve creates Db file
# pickle loads the whole object into the memory as it sees the open()
# shelve stores the object like a dictionary where the value is not loaded into a memory rather it is in a file.
# on windows it creates 3 different files .bak .dat .dir
# Difference between a shelve and a dictionary is - in shelve a key is always a string

import shelve

# with shelve.open('shelveFile') as fruit:
#     fruit['orange'] = 'a sweet orange citrus fruit'
#     fruit['apple'] = ' a fruit good for cider'
#     fruit['lemon'] = ' a citrus fruit'
#
#     print(fruit['apple'])
with shelve.open('shelveFile') as fruit:
    fruit['banana'] = "full of pottasium"
    print(fruit)
    for f in fruit.keys():
        print(fruit[f])