# need to add the downloaded cards image in the project directory

import tkinter
import random


def load_images(card_images):
    suits = ['hearts', 'clubs', 'diamonds', 'spades']
    face_cards = ['jack', 'queen', 'king']

    for suit in suits:
        for card in range(1, 11):
            name = 'SVG-cards-1.1/svg/{}_of_{}.{}'.format('0'+str(card), suit, 'svg')
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        for card in face_cards:
            name = 'SVG-cards-1.1/svg/{}_of{}.{}'.format(str(card), suit, 'svg')
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

# The follwing function is called by the button to deal with the cards


def deal_card(frame):
    # pop the next card off the deck
    next_card = deck.pop()
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side="left")
    return next_card


def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)


mainWindow = tkinter.Tk()
# adding title to the window
mainWindow.title("Welcome to BlackJack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images for dealer

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images for Player
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow).grid(row=3, column=0, sticky="w", columnspan=3)

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer()).grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text="Player", command=deal_player()).grid(row=0, column=1)

# calling load function from here

cards = []
load_images(cards)
print(cards)

mainWindow.mainloop()
