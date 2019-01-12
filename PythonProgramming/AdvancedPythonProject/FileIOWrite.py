cities = ["Delhi", "Bangalore", "Pune", "Kolkata", "Hyderabad", "Chandigarh"]

# Key thing to notice here is that file=city_file is passed as a named argument but not a value to it hence it does not
# spaces around file

# The data is written to a buffer from where it is in the background written in a text  file.

# Python 3 in 2008 has come up with a Flush parameter which speeds up the data writing process on a slow device.

# with open('cityFile.txt', 'w') as city_file:
#     for city in cities:
#         #print(city, file=city_file)
#         print(city, file=city_file, flush=True)

citiesRead = []

with open('cityFile.txt', 'r') as cities:
    for city in cities:
        print(city, end='')