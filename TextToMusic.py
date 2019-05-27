from Resources import Progression, GUI


def play_prog():
    progression.phrase = gui.phrase.get()
    progression.create_inputs()
    chord_array = progression.edit_progression()
    gui.chords_display.config(text=" / ".join(chord_array[0]))
    progression.play_progression()
    gui.play_prog_button.config(state='normal')
    return gui.export_prog_button.config(state='normal')


def export_prog():
    gui.info.config(text="Exporting...")
    progression.export_progression()
    return gui.info.config(text="Done.")


if __name__ == '__main__':
    gui = GUI(play_func=play_prog, exp_func=export_prog)
    progression = Progression()
    gui.display_window()
    gui.mainloop()
