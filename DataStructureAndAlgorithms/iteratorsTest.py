import random


strings = "!@#$^*_-=+?/,.:;~"
grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]


face_emojis_list = [random.choice(strings) for _ in range(3)]
face_strings = "".join(face_emojis_list)
emoticon = (random.choice(grouped_strings)[0], face_strings, random.choice(grouped_strings)[1])
emoticon = "".join(emoticon)

print(face_emojis_list)
print(emoticon)

print(["Hello" for _ in range(10)])

######################## Iterator test #############################


def vowels():
    yield("a")
    yield ("e")
    yield ("i")
    yield ("o")
    yield ("u")


for i in vowels():
    print(i)
