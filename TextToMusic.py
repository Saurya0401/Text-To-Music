import _thread  # TODO: Use threading instead
import playsound
import random
from tkinter import *
from Progressions import Progressions


chord_dict = {1: "A", 2: "A#", 3: "B", 4: "C", 5: "C#", 6: "D", 7: "D#", 8: "E", 9: "F", 10: "F#", 11: "G",
              12: "G#", 13: "Am", 14: "A#m", 15: "Bm", 16: "Cm", 17: "C#m", 18: "Dm", 19: "D#m", 20: "E#m",
              21: "Fm", 22: "F#m", 23: "Gm", 24: "G#m"}


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

    # Deletes extra chords or adds them
    if char_count < chord_count:
        del progression.chords[char_count:]
    elif chord_count < char_count:
        extra_chords = []
        difference = char_count - chord_count
        for _ in range(0, difference):
            extra_chords.append(random.choice(progression.chords))
        progression.extra = extra_chords
        progression.add_chords()

    chords_playing = []
    for i in progression.chords:
        if i in chord_dict.keys():
            chords_playing.append(chord_dict[i])
        filename = "audio files/{}__{}.wav".format(num_1[i-1], num_2[i-1])
        playsound.playsound(filename)
    chords_display.insert(END, chords_playing)


root = Tk()
root.title("Text to Music")
input_frame = Frame(root)
input_frame.grid(row=0)
text_field_name = Label(input_frame, text="Enter phrase: ")
text_field_name.grid(row=0, column=0, padx=5)
text_field = Entry(input_frame)
text_field.grid(row=0, column=1)
play_prog_button = Button(input_frame, text="Play Progression!",
                          command=lambda: _thread.start_new_thread(text_to_music, (text_field.get(),)), bg="blue",
                          fg="white")
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
