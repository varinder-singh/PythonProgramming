# Sets are 4th type of data structure in python.
# Does not contain duplicates
# Sets are unordered and elements are hashed before they are stored.
# Immutable objects
# Union and intersection operations on set objects

farmAnimals = {"sheep", "cow", "hen"}
wildAnimals = set(["lion", "tiger", "panther"])

print(farmAnimals)
print("=" * 40)
print(wildAnimals)

farmAnimals.add("horse")
wildAnimals.add("horse")

print(farmAnimals)
print("=" * 40)
print(wildAnimals)