import time
import tkinter as tk
from tkinter import PhotoImage
from game import Game

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

NUMBER_OF_CARDS = 5
NUMBER_OF_PLAYERS = 2

class ApplicationGui(tk.Frame):

    game_engine = None
    var = []

    def __init__(self, master=None):
        super().__init__(master)
        self.images = {"H": PhotoImage(file="images/heart.png"),
                       "C": PhotoImage(file="images/club.png"),
                       "S": PhotoImage(file="images/spade.png"),
                       "D": PhotoImage(file="images/diamond.png"),
                       "Blank" : PhotoImage(file="images/blank.png")}
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_hand_label = tk.Label(self, text = "My hand:")
        self.my_hand_label.grid(row = 0, column = 0, sticky = tk.constants.W) # Left alignment (West)
        self.my_hand = []

        self.your_hand_label = tk.Label(self, text="Your hand:")
        self.your_hand_label.grid(row = 1, column = 0, sticky = tk.constants.W) # Left alignment (West)
        self.your_hand = []

        for i in range(NUMBER_OF_CARDS):
            self.my_hand.append(tk.Label(self,
                                         image = self.images["Blank"],
                                         width = 90, height = 90,
                                         compound = tk.constants.CENTER,
                                         fg="white"))
            self.my_hand[i].grid(row = 0, column = i + 1, sticky = tk.constants.W)  # Left alignment (West)
            var = tk.IntVar()
            self.your_hand.append((tk.Checkbutton(self,
                                                  image = self.images["Blank"],
                                                  width = 90, height = 90,
                                                  compound = tk.constants.CENTER,
                                                  fg = "white",
                                                  indicatoron = False,
                                                  state = tk.constants.DISABLED,
                                                  variable = var),
                                   var))
            self.your_hand[i][0].grid(row = 1, column = i + 1, sticky = tk.constants.W)  # Left alignment (West)


        self.deal_cards_button = tk.Button(self,
                                           text = "Deal Cards",
                                           height = 3,
                                           width = 30,
                                           command = self.deal_cards)
        self.deal_cards_button.grid(row = 2, column = 0, columnspan = 4)

        self.new_cards_button = tk.Button(self,
                                          text = "Get New Cards",
                                          height = 3,
                                          width = 30,
                                          command = self.get_new_cards,
                                          state = tk.constants.DISABLED)
        self.new_cards_button.grid(row = 2, column = 4, columnspan = 4)

        self.quit = tk.Button(self,
                              text = "QUIT",
                              fg = "red",
                              command = root.destroy)
        self.quit.grid(row = 3, column = 1, columnspan = 3)

    def assign_game_engine(self, game_engine):
        self.game_engine = game_engine

    def get_new_cards(self):
        dropped_cards = []

        for button, var in self.your_hand:
            if var.get() == 1: #checked
                print("{} changed.".format(button["text"]))
                button["image"] = self.images["Blank"]
                button["state"] = tk.constants.DISABLED
                dropped_cards.append(button["text"])
                button["text"] = ""

        more_tries, new_cards = self.game_engine.get_new_cards(dropped_cards)
        print(new_cards)
        for new_card in new_cards:
            for button, var in self.your_hand:
                if var.get() == 1: #checked
                    button["text"] = new_card
                    button["image"] = self.images[new_card[-1]]
                    button["state"] = tk.constants.NORMAL
                    button.deselect()
                    break

        if not more_tries:
            for button, var in self.your_hand:
                button["state"] = tk.constants.NORMAL
            self.new_cards_button["state"] = tk.constants.DISABLED
            for label in self.my_hand:
                label["image"] = self.images[label["text"][-1]]
            print("GAME OVER!")

    def deal_cards(self):
        self.new_cards_button["state"] = tk.constants.NORMAL
        hands = game_engine.deal_cards(NUMBER_OF_PLAYERS, NUMBER_OF_CARDS)
        for button in self.my_hand:
            button["state"] = tk.constants.NORMAL
        for button, var in self.your_hand:
            button["state"] = tk.constants.NORMAL

        if hands != None:
            for i in range(NUMBER_OF_CARDS):
                self.my_hand[i]["text"] = hands[0][i]
                self.my_hand[i]["image"] = self.images["Blank"]
                self.your_hand[i][0]["text"] = hands[1][i]
                self.your_hand[i][0]["image"] = self.images[hands[1][i][-1]]

root = tk.Tk()
root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
app = ApplicationGui(master = root)

game_engine = Game()
app.assign_game_engine(game_engine)

app.mainloop()
