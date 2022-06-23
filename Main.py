import tkinter as tk
from tkinter import *


def adlibs_with_eve():

    adlibs_with_eve_game_window = tk.Tk()
    adlibs_with_eve_game_window.title("Adlibs with Eve!")
    adlibs_with_eve_game_window.iconbitmap('C:\Code Projects\Eve\Eve Core\Eve.ico')

    def adlibs_with_eve_data_entry1():

        global great_label
        global favourite_colour_label
        global favourite_colour_entry
        global favourite_colour_enter


        great_label = Label(adlibs_with_eve_game_window, \
                            text="Let's make a story together and let's make that story special to you!")

        great_label.pack()

        favourite_colour_label = Label(adlibs_with_eve_game_window, text="Your favourite colour:")

        favourite_colour_entry = Entry(adlibs_with_eve_game_window)
        favourite_colour_enter = Button(adlibs_with_eve_game_window, \
                                        text="Enter", command=adlibs_with_eve_data_entry2)

        favourite_colour_label.pack()
        favourite_colour_entry.pack()
        favourite_colour_enter.pack()

    def adlibs_with_eve_data_entry2():

        global second_favourite_colour_label
        global second_favourite_colour_entry
        global second_favourite_colour_enter

        great_label.pack_forget()
        favourite_colour_label.pack_forget()
        favourite_colour_entry.pack_forget()
        favourite_colour_enter.pack_forget()
        adlibs_with_eve_data_entry1_pause1.pack_forget()
        adlibs_with_eve_data_entry1_pause2.pack_forget()

        favourite_colour_token = open("favourite_colour_token.txt", "w")

        favourite_colour_token.write(favourite_colour_entry.get())

        favourite_colour_token.close()

        second_favourite_colour_label = Label(adlibs_with_eve_game_window, text="Your second favourite colour:")
        second_favourite_colour_entry = Entry(adlibs_with_eve_game_window)
        second_favourite_colour_enter = Button(adlibs_with_eve_game_window, text="Enter", \
                                               command=adlibs_with_eve_data_entry3)

        second_favourite_colour_label.pack()
        second_favourite_colour_entry.pack()
        second_favourite_colour_enter.pack()

    def adlibs_with_eve_data_entry3():

        global something_you_like_label
        global something_you_like_entry
        global something_you_like_enter

        second_favourite_colour_label.pack_forget()
        second_favourite_colour_entry.pack_forget()
        second_favourite_colour_enter.pack_forget()
        adlibs_with_eve_data_entry1_pause1.pack_forget()
        adlibs_with_eve_data_entry1_pause2.pack_forget()

        second_favourite_colour_token = open("second_favourite_colour_token.txt", "w")

        second_favourite_colour_token.write(second_favourite_colour_entry.get())

        second_favourite_colour_token.close()

        something_you_like_label = Label(adlibs_with_eve_game_window, text="Something you like:")
        something_you_like_entry = Entry(adlibs_with_eve_game_window)
        something_you_like_enter = Button(adlibs_with_eve_game_window, text="Enter",
                                          command=adlibs_with_eve_data_entry4)

        something_you_like_label.pack()
        something_you_like_entry.pack()
        something_you_like_enter.pack()

    def adlibs_with_eve_data_entry4():

        global someone_you_love_label
        global someone_you_love_entry
        global someone_you_love_enter

        something_you_like_label.pack_forget()
        something_you_like_entry.pack_forget()
        something_you_like_enter.pack_forget()
        adlibs_with_eve_data_entry1_pause1.pack_forget()
        adlibs_with_eve_data_entry1_pause2.pack_forget()

        something_you_like_token = open("something_you_like_token.txt", "w")

        something_you_like_token.write(something_you_like_entry.get())

        something_you_like_token.close()

        someone_you_love_label = Label(adlibs_with_eve_game_window, text="Someone you love:")
        someone_you_love_entry = Entry(adlibs_with_eve_game_window)
        someone_you_love_enter = Button(adlibs_with_eve_game_window, text="Enter",
                                        command=adlibs_with_eve_data_execution)

        someone_you_love_label.pack()
        someone_you_love_entry.pack()
        someone_you_love_enter.pack()

    def adlibs_with_eve_data_execution():

        global adlibs_ending_button
        global roses_are_label
        global violets_are_label
        global i_like_label
        global i_love_label
        global adlibs_ending_label
        global here_we_go_label

        someone_you_love_token = open("someone_you_love_token.txt", "w")

        someone_you_love_token.write(someone_you_love_entry.get())

        someone_you_love_token.close()

        someone_you_love_label.pack_forget()
        someone_you_love_entry.pack_forget()
        someone_you_love_enter.pack_forget()
        adlibs_with_eve_data_entry1_pause1.pack_forget()
        adlibs_with_eve_data_entry1_pause2.pack_forget()

        here_we_go_label = Label(adlibs_with_eve_game_window, text="Here we go!")

        here_we_go_label.pack()

        adlibs_with_eve_data_execution_pause1.pack()

        roses_are_label = Label(adlibs_with_eve_game_window, text="Roses are " + favourite_colour_entry.get() + ",")
        violets_are_label = Label(adlibs_with_eve_game_window, text="Violets are " \
                                                                    + second_favourite_colour_entry.get() + ",")
        i_like_label = Label(adlibs_with_eve_game_window, text="I like " + something_you_like_entry.get() + ",")
        i_love_label = Label(adlibs_with_eve_game_window, text="And I love " + someone_you_love_entry.get() + "!")

        roses_are_label.pack()
        violets_are_label.pack()
        i_like_label.pack()
        i_love_label.pack()

        adlibs_with_eve_data_execution_pause2.pack()

        adlibs_ending_label = Label \
            (adlibs_with_eve_game_window, \
             text="Well, it doesn't really rhyme, but I'm sure " + someone_you_love_entry.get() + " would like it!")
        adlibs_ending_label.pack()

    adlibs_with_eve_data_entry1()

    adlibs_with_eve_game_window.mainloop()


adlibs_with_eve()
