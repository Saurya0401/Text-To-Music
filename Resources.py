import tkinter as tk
import _thread
import random


class Progression:
    """
    This class contains all the methods and relevant variables needed to generate chord progressions.

    NOTE: Henceforth, the numerical values of the chords will be referred to as "CNV (Chord Numerical Value)".

    Class Variables
    ---------------
    There are four class variables, 'first_chords', 'extension_dict', 'chord_dict' and 'chords_playing'.
    'first_chords' is a purely numerical list and the CNV of the first chord of every progression will belong to this
    list.
    'extension_dict' is a dictionary and is used to generate the next few CNVs of a progression depending on what the
    first chord was.
    'chord_dict' is a dictionary and is used to translate CNVs to chords.
    'chords_playing' is a purely numerical list that is initialised empty. When 'insert_chords_to_display(self)' is
    called, all the CNVs in 'self.chords' are appended to this list. It is used to display chords in the GUI window.
    """

    first_chords = [int(i) for i in range(1, 25)]
    extension_dict = {1: [8, 22, 6], 2: [7, 2, 23], 3: [10, 24, 19, 8, 3, 8, 22], 4: [11, 13, 9], 5: [24, 14, 10],
                      6: [1, 15, 22, 11, 6, 11, 1], 7: [2, 15, 12], 8: [3, 17, 24, 1, 8, 1, 3], 9: [4, 18, 2],
                      10: [5, 19, 3], 11: [4, 6, 8], 12: [7, 20, 5], 13: [9, 4, 11], 14: [19, 5, 10], 15: [11, 6, 1],
                      16: [11, 12, 2, 9, 16, 9, 11], 17: [1, 8, 3], 18: [2, 9, 4], 19: [3, 10, 5], 20: [4, 11, 6],
                      21: [16, 5, 14], 22: [6, 1, 8], 23: [7, 2, 9], 24: [8, 3, 10]}
    chord_dict = {1: "A", 2: "A#", 3: "B", 4: "C", 5: "C#", 6: "D", 7: "D#", 8: "E", 9: "F", 10: "F#", 11: "G",
                  12: "G#", 13: "Am", 14: "A#m", 15: "Bm", 16: "Cm", 17: "C#m", 18: "Dm", 19: "D#m", 20: "E#m",
                  21: "Fm", 22: "F#m", 23: "Gm", 24: "G#m"}
    chords_playing = []

    def __init__(self, phrase, first_chord, chords=None, extra=None, num_1=None, num_2=None):
        """
        :param phrase: This is the input provided by the user. The input is a string.
        :param first_chord: This is the CNV of the first chord of a progression. This is provided by the main script and
         is a random integer between 1 and 24.
        :param chords: Initially empty list. Based on how the progression is generated and managed, CNVs
        are likewise appended and removed from this list.
        :param extra: Initially empty list. The method "manage_chords()" adds CNVs to this list if needed. The
        contents of this list are ultimately merged with 'self.chords'.
        :param num_1: A list of integers from 47845 to 47868. These numbers are part of the filename.
        :param num_2: A list of integers from 1 to 24. These numbers are part of the filename.
        """

        self.phrase = phrase
        self.characters = [i for i in self.phrase if i != " "]
        self.first_chord = first_chord
        if chords is None:
            self.chords = []
        else:
            self.chords = chords
        if extra is None:
            self.extra = []
        else:
            self.extra = extra
        if num_1 is None:
            self.num_1 = []
        else:
            self.num_1 = num_1
        if num_2 is None:
            self.num_2 = []
        else:
            self.num_2 = num_2

    def add_chords(self):
        """
        Appends the contents of 'self.extra' to 'self.chords'.
        """

        self.chords.extend(self.extra)

    def generate_progression(self):
        """
        This method first checks and compares the value of 'self.first_chord' to the keys in 'extension_dict'.
        It then appends the CNVs of the matching key to 'self.chords'.
        """

        if self.first_chord in Progression.first_chords:
            self.chords.extend(Progression.extension_dict[self.first_chord])

    def insert_chords_to_display(self):
        """
        This method iterates over every CNV in 'self.chords' and compares them with the keys in 'chord_dict'.
        Then it appends all the relevant CNVs in 'self.chords' to 'chords_playing'.
        """

        for i in self.chords:
            if i in Progression.chord_dict.keys():
                Progression.chords_playing.append(Progression.chord_dict[i])

    def manage_chords(self):
        """
        This method either deletes CNVs from 'self.chords' if the number of CNVs exceeds the character count in
        'self.phrase', or appends more CNVs to 'self.chords' if the character count in 'self.phrase' exceeds the number
        of pre-determined CNVs in the current progression. In the latter case, the extra CNVs added are randomly chosen
        from the CNVs in the current progression.
        """

        char_count = len(self.phrase)
        chord_count = len(self.chords)
        if chord_count > char_count:
            del self.chords[char_count:]
        elif chord_count < char_count:
            deficit = char_count - chord_count
            extra_chords = []
            for _ in range(0, deficit):
                extra_chords.append(random.choice(self.chords))
            self.extra = extra_chords
            self.add_chords()


class GUI(tk.Tk):
    """
    This class contains the methods needed to display and control the GUI window using tkinter.
    """

    def __init__(self, func, chords):
        """
        :param func: This is the main function that is passed in.
        :param chords: Initially empty list. When the GUI window is initiated, the contents of this list become
        identical to the contents of the variable 'chords_playing' in the class 'Progression'.
        """

        tk.Tk.__init__(self)
        GUI.title(self, "Text To Music")
        self.func = func
        self.chords = chords

        # Start defining GUI components
        self.input_frame = tk.Frame(self)
        self.input_frame.grid(row=0)
        self.output_frame = tk.Frame(self)
        self.output_frame.grid(row=1)
        self.text_field_name = tk.Label(self.input_frame, text="Enter phrase: ")
        self.text_field_name.grid(row=0, column=0, padx=5)
        self.text_field = tk.Entry(self.input_frame)
        self.text_field.grid(row=0, column=1)
        self.play_prog_button = tk.Button(self.input_frame, text="Play Progression!", command=lambda: _thread.
                                          start_new_thread(func, ()), bg="blue", fg="white")
        self.play_prog_button.grid(row=0, column=2, padx=5)
        self.chord_title = tk.Label(self.output_frame, text="Chords in this progression: ")
        self.chord_title.grid(row=0, column=0)
        self.chords_display = tk.Text(self.output_frame, height=2, width=40)
        self.chords_display.grid(row=1, column=0)
        self.scrollbar = tk.Scrollbar(self.output_frame)
        self.scrollbar.grid(row=1, column=2)
        self.chords_display.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.chords_display.yview)
        # Finished defining GUI components

    def clear_chords_display(self):
        """
        This method resets 'self.chords_display'.
        """

        self.chords_display.delete('1.0', tk.END)

    def display_chords(self):
        """
        This method inserts the contents of 'self.chords' into 'self.chords_display'. Essentially it displays the actual
        chords in the GUI window.
        """

        self.chords[-1] += "/"
        self.chords_display.insert(tk.END, self.chords)

    def disable_prog_button(self):
        """
        This method disables 'self.play_prog_button' when it is called.
        """

        self.play_prog_button.config(state="disabled")

    def enable_prog_button(self):
        """
        This method re-enables 'self.play_prog_button' when it is called.
        """
        
        self.play_prog_button.config(state="normal")
