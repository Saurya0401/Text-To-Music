import playsound
import random
from Resources import Progression, GUI


def main():
    """
    This function is responsible for correctly generating the progression as well as managing both the progression and
    part of the GUI window.
    """

    # reset the GUI chords display and disable play_prog_button
    display_window.clear_chords_display()
    display_window.button_status(display_window.play_prog_button, 0)

    # generate non-user inputs
    start_chord = random.randint(1, 24)
    serial_number = range(47845, 47869)
    chord_number = range(1, 25)

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
        try:
            filename = "audio files/{}__{}.wav".format(progression.num_1[i-1], progression.num_2[i - 1])
            playsound.playsound(filename)
        except FileNotFoundError:
            print('Error: audio files not found.')

    # re-enable play_prog_button and 'export_prog_button'.
    display_window.button_status(display_window.play_prog_button, 1)
    display_window.button_status(display_window.export_prog_button, 1)

    # Enable progression to be exported to XML
    display_window.exp_func = progression.export_progression()


# generate the GUI window
display_window = GUI(main, Progression.chords_playing)
display_window.mainloop()
