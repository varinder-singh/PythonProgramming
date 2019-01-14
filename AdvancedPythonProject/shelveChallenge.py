# convert a dictionary object into a shelve.
# just to show how a complex object can be shelved

import shelve

books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                     "beans_ont_toast": ["beans", "bread"],
                     "scrambled_eggs": ["eggs", "butter", "milk"],
                     "soup": ["tin of soup"],
                     "pasta": ["pasta", "cheese"]},
         "maintenace": {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}}

#print(books["recipes"]["scrambled_eggs"])

with shelve.open("ShelveChallengeFile") as scf:
    #scf["book"] = books
    for item in scf.items():
        print(item)