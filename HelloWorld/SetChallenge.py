# Create a Program that takes the text and returns a list of all the chars that are not vowels

myString = "my name is Vairndere"

myVowels = {'a', 'e', 'i', 'o', 'u'}

myList = list()

result = set(myString).difference(myVowels)

print(result)