# Iterators are objects to iterate on iterable objects such as strings, lists and tuples

# For and while implicitly creates and iterator from itrable object and stop iteration at the last element

value = "0123456789"

myIterator = iter(value)

# for x in range(0, len(value)):
#     next_item = next(myIterator)
#     print(next_item)

while(next(myIterator)):
    next_item = next(myIterator)
    print(next_item)