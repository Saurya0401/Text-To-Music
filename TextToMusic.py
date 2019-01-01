# import threading
import _thread
import playsound
import random
from tkinter import *
from Progressions import Progressions, A, AS, B, C, CS, D, DS, E, F, FS, G, GS


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

    progression = Progressions(start_chord, None, None)

    if start_chord in [1, 13]:
        progression = A(start_chord, [start_chord])
        if start_chord == 1:
            progression.AEFSmD_progression()
        elif start_chord == 13:
            progression.AmFCG_progression()
    elif start_chord in [2, 14]:
        progression = AS(start_chord, [start_chord])
        if start_chord == 2:
            progression.ASDSASGm_progression()
        elif start_chord == 14:
            progression.ASmDSmCSFS_progression()
    elif start_chord in [3, 15]:
        progression = B(start_chord, [start_chord])
        if start_chord == 3:
            progression.BFSGSmDSmEBEFSm_progression()
        elif start_chord == 15:
            progression.BmGDA_progression()
    elif start_chord in [4, 16]:
        progression = C(start_chord, [start_chord])
        if start_chord == 4:
            progression.CGAmF_progression()
        elif start_chord == 16:
            progression.CmGmGSDSFmCmFmGm_progression()
    elif start_chord in [5, 17]:
        progression = CS(start_chord, [start_chord])
        if start_chord == 5:
            progression.CSGSASmFS_progression()
        elif start_chord == 17:
            progression.CSmAEB_progression()
    elif start_chord in [6, 18]:
        progression = D(start_chord, [start_chord])
        if start_chord == 6:
            progression.DABmFSmGDGA_progression()
        elif start_chord == 18:
            progression.DmASFC_progression()
    elif start_chord in [7, 19]:
        progression = DS(start_chord, [start_chord])
        if start_chord == 7:
            progression.DSASBmGS_progression()
        elif start_chord == 19:
            progression.DSmBFSCS_progression()
    elif start_chord in [8, 20]:
        progression = E(start_chord, [start_chord])
        if start_chord == 8:
            progression.EBCSmGSmAEAB_progression()
        elif start_chord == 20:
            progression.EmCGD_progression()
    elif start_chord in [9, 21]:
        progression = F(start_chord, [start_chord])
        if start_chord == 9:
            progression.FCDmAS_progression()
        elif start_chord == 21:
            progression.FmCmCSASm_progression()
    elif start_chord in [10, 22]:
        progression = FS(start_chord, [start_chord])
        if start_chord == 10:
            progression.FSCSDSmB_progression()
        elif start_chord == 22:
            progression.FSmDAE_progression()
    elif start_chord in [11, 23]:
        progression = G(start_chord, [start_chord])
        if start_chord == 11:
            progression.GCDE_progression()
        elif start_chord == 23:
            progression.GmDSASF_progression()
    elif start_chord in [12, 24]:
        progression = GS(start_chord, [start_chord])
        if start_chord == 12:
            progression.GSDSEmCS_progression()
        elif start_chord == 24:
            progression.GSmEBFS_progression()

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

    # print("Playing chords: ")
    chords_playing = []
    for i in progression.chords:
        if i in num_to_chord().keys():
            chords_playing.append(num_to_chord()[i])
        # print(", ".join(str(x) for x in chords_playing))
        filename = "audio files/{}__{}.wav".format(num_1[i-1], num_2[i-1])
        playsound.playsound(filename)
    chords_display.insert(END, chords_playing)


# if __name__ == '__main__':
#     text_to_music(str(input("Enter phrase: "))))

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
# GUI = GUIThread(text_field.get())
# play_prog_button = Button(input_frame, text="Play Progression!", command=GUI.start(), bg="blue", fg="white")
# play_prog_button.grid(row=0, column=2, padx=5)
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
#
#
# root.mainloop()