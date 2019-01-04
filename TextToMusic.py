# import threading
import _thread
import playsound
import random
from tkinter import *
from Progressions import Progressions


def num_to_chord():
    num = [i for i in range(1, 25)]
    chords = [i for i in "A A# B C C# D D# E F F# G G# Am A#m Bm Cm C#m Dm D#m Em Fm F#m Gm G#m".split(" ")]
    chord_dict = {}
    for i in range(0, 24):
        chord_dict.update({num[i]: chords[i]})
    return chord_dict


def text_to_music(phrase):
    chords_display.delete('1.0', END)
    characters = [i for i in phrase if i != " "]
    char_count = len(characters)

    num_1 = [int(x) for x in range(47845, 47869)]
    num_2 = [int(y) for y in range(1, 25)]

    start_chord = random.randint(1, 24)

    progression = Progressions(start_chord, [start_chord], None)

    progression.generate_progression()

    chord_count = len(progression.chords)

    # Deletes extra chords if len(chords) exceeds char_count and adds extra chords if char_count exceeds len(chords)
    if char_count < chord_count:
        del progression.chords[char_count:]
    elif chord_count < char_count:
        extra_chords = []
        difference = char_count - chord_count
        for _ in range(0, difference):
            extra_chords.append(random.choice(progression.chords))
        progression.extra = extra_chords
        progression.add_chords()

    # print(str(progression.chords))                    for console
    # print("Playing chords: ")                         for console
    chords_playing = []
    for i in progression.chords:
        if i in num_to_chord().keys():
            chords_playing.append(num_to_chord()[i])
        filename = "audio files/{}__{}.wav".format(num_1[i-1], num_2[i-1])
        playsound.playsound(filename)
    # print(", ".join(str(x) for x in chords_playing))  for console
    chords_display.insert(END, chords_playing)


# if __name__ == '__main__':                            for console
#     text_to_music(str(input("Enter phrase: ")))       for console

root = Tk()
root.title("Text to Music")
input_frame = Frame(root)
input_frame.grid(row=0)
text_field_name = Label(input_frame, text="Enter phrase: ")
text_field_name.grid(row=0, column=0, padx=5)
text_field = Entry(input_frame)
text_field.grid(row=0, column=1)
play_prog_button = Button(input_frame, text="Play Progression!", command=lambda: _thread.start_new_thread(text_to_music, (text_field.get(),)), bg="blue", fg="white")
play_prog_button.grid(row=0, column=2, padx=5)
output_frame = Frame(root)
output_frame.grid(row=1)
chord_title = Label(output_frame, text="Chords in this progression: ")
chord_title.grid(row=0, column=0)
chords_display = Text(output_frame, height=2, width=40)
chords_display.grid(row=1, column=0)
scrollbar = Scrollbar(output_frame)
scrollbar.grid(row=1, column=2)
chords_display.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=chords_display.yview)


root.mainloop()

# TODO: Figure out the correct code that'll run with threading instead of _thread
# class GUIThread(threading.Thread):
#     def __init__(self, text_output):
#         threading.Thread.__init__(self)
#         self.text_output = text_output
#
#     def run(self):
#         text_to_music(self.text_output)
#
#
# root = Tk()
# root.title("Text to Music")
# input_frame = Frame(root)
# input_frame.grid(row=0)
# text_field_name = Label(input_frame, text="Enter phrase: ")
# text_field_name.grid(row=0, column=0, padx=5)
# text_field = Entry(input_frame)
# text_field.grid(row=0, column=1)
# output_frame = Frame(root)
# output_frame.grid(row=1)
# chord_title = Label(output_frame, text="Chords in this progression: ")
# chord_title.grid(row=0, column=0)
# chords_display = Text(output_frame, height=2, width=40)
# chords_display.grid(row=1, column=0)
# scrollbar = Scrollbar(output_frame)
# scrollbar.grid(row=1, column=2)
# chords_display.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=chords_display.yview)
# phrase = text_field.get()
# GUI = GUIThread(phrase)
# play_prog_button = Button(input_frame, text="Play Progression!", command=GUI.start(), bg="blue", fg="white")
# play_prog_button.grid(row=0, column=2, padx=5)
#
#
# root.mainloop()