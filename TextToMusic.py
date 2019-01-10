import playsound
import random
from Resources import Progression, GUI


def main():
    """
    This function is responsible for correctly generating the progression as well as managing both the progression and
    parts of the GUI window.
    """

    # reset the part of the GUI that displays chords
    display_window.clear_chords_display()

    # generate non-user inputs
    start_chord = random.randint(1, 24)
    serial_number = [int(x) for x in range(47845, 47869)]
    chord_number = [int(y) for y in range(1, 25)]

    # create a progression as an instance of the 'Progression' class
    progression = Progression(display_window.text_field.get(), start_chord, [start_chord], [], serial_number,
                              chord_number)

    # manage the progression by calling the class methods in the correct order
    progression.generate_progression()
    progression.manage_chords()
    progression.insert_chords_to_display()

    # call the method that displays the chords in the GUI window
    display_window.display_chords()

    # iterate over every value in 'progression.chords' and play the matching audio file
    for i in progression.chords:
        filename = "audio files/{}__{}.wav".format(progression.num_1[i-1], progression.num_2[i - 1])
        playsound.playsound(filename)


# generate the GUI window
display_window = GUI(main, Progression.chords_playing)
display_window.mainloop()

