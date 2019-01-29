import tkinter as tk
import _thread
import random
import lxml.etree as et
from os import path, mkdir
from datetime import datetime
from tkinter import filedialog


class Progression:
    """
    This class contains all the methods and relevant variables needed to generate chord progressions.

    NOTE: Henceforth, the numerical values of the chords will be referred to as "CNV (Chord Numerical Value)".

    Class Variables
    ---------------
    There are four class variables, 'first_chords', 'extension_dict', 'chord_dict' and 'chords_playing'.
    'first_chords' is a purely numerical list and the CNV of the first chord of every progression will be from this
    list.
    'extension_dict' is a dictionary and is used to generate the next few CNVs of a progression depending on what the
    first chord was.
    'chord_dict' is a dictionary and is used to translate CNVs to chords.
    'prog_dict' is a dictionary where the keys are the CNVs of all the first chords and their corresponding values are
    all lists containing every progression in chord form. It is used to identify a progression from the first chord.
    'chords_playing' is a purely numerical list that is initialised empty. When 'insert_chords_to_display(self)' is
    called, all the CNVs in 'self.chords' are translated using 'chord_dict' and  appended to this list. It is used to
    display chords in the GUI window.
    'timestamp' is self-explanatory.
    """

    first_chords = [int(i) for i in range(1, 25)]
    extension_dict = {1: [8, 22, 6], 2: [7, 2, 23], 3: [10, 24, 19, 8, 3, 8, 22], 4: [11, 13, 9], 5: [24, 14, 10],
                      6: [1, 15, 22, 11, 6, 11, 1], 7: [2, 15, 12], 8: [3, 17, 24, 1, 8, 1, 3], 9: [4, 18, 2],
                      10: [5, 19, 3], 11: [4, 6, 8], 12: [7, 20, 5], 13: [9, 4, 11], 14: [19, 5, 10], 15: [11, 6, 1],
                      16: [11, 12, 2, 9, 16, 9, 11], 17: [1, 8, 3], 18: [2, 9, 4], 19: [3, 10, 5], 20: [4, 11, 6],
                      21: [16, 5, 14], 22: [6, 1, 8], 23: [7, 2, 9], 24: [8, 3, 10]}
    chord_dict = {1: "A", 2: "A#", 3: "B", 4: "C", 5: "C#", 6: "D", 7: "D#", 8: "E", 9: "F", 10: "F#", 11: "G",
                  12: "G#", 13: "Am", 14: "A#m", 15: "Bm", 16: "Cm", 17: "C#m", 18: "Dm", 19: "D#m", 20: "Em",
                  21: "Fm", 22: "F#m", 23: "Gm", 24: "G#m"}
    prog_dict = {1: ['A', 'E', 'F#m', 'D'], 2: ['A#', 'D#', 'A#', 'Gm'],
                 3: ['B', 'F#', 'G#m', 'D#m', 'E', 'B', 'E', 'F#m'], 4: ['C', 'G', 'Am', 'F'],
                 5: ['C#', 'G#m', 'A#m', 'F#'], 6: ['D', 'A', 'Bm', 'F#m', 'G', 'D', 'G', 'A'],
                 7: ['D#', 'A#', 'Bm', 'G#'], 8: ['E', 'B', 'C#m', 'G#m', 'A', 'E', 'A', 'B'],
                 9: ['F', 'C', 'Dm', 'A#'], 10: ['F#', 'C#', 'D#m', 'B'], 11: ['G', 'C', 'D', 'E'],
                 12: ['G#', 'D#', 'Em', 'C#'], 13: ['Am', 'F', 'C', 'G'], 14: ['A#m', 'D#m', 'C#', 'F#'],
                 15: ['Bm', 'G', 'D', 'A'], 16: ['Cm', 'G', 'G#', 'A#', 'F', 'Cm', 'F', 'G'],
                 17: ['C#m', 'A', 'E', 'B'], 18: ['Dm', 'A#', 'F', 'C'], 19: ['D#m', 'B', 'F#', 'C#'],
                 20: ['Em', 'C', 'G', 'D'], 21: ['Fm', 'Cm', 'C#', 'A#m'], 22: ['F#m', 'D', 'A', 'E'],
                 23: ['Gm', 'D#', 'A#', 'F'], 24: ['G#m', 'E', 'B', 'F#']}
    chords_playing = []
    timestamp = datetime.now()

    def __init__(self, phrase, first_chord, chords=None, extra=None, num_1=None, num_2=None):
        """
        :param phrase: This is the input provided by the user. It is a string.
        :param first_chord: This is the CNV of the first chord of a progression. It is provided by the main script and
        is a random integer between 1 and 24.
        :param chords: Initially only contains the CNV of the first chord of the progression. Based on how the
        progression is generated and managed, CNVs are likewise appended and removed from this list.
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
        self.prog_id = [i for i in self.prog_dict[self.first_chord] if i != "/"]

    def add_chords(self):
        """
        Appends the contents of 'self.extra' to 'self.chords'.
        """

        self.chords.extend(self.extra)

    def export_progression(self):
        """
        This method exports the chords in 'self.chords_playing' as an XML file.
        """

        root = et.Element('progression')
        cnv = et.SubElement(root, 'CNV')
        cnv.text = " ".join(str(i) for i in self.chords)
        p_type = et.SubElement(root, 'type')
        p_type.text = "{} {}".format(" ".join(self.prog_id), "progression")
        chords = et.SubElement(root, 'chords')
        chords.text = " - ".join(i for i in self.chords_playing if i != "/")
        export_data = et.tostring(root, encoding='unicode', pretty_print=True)
        filename = "{} ".format("".join(self.prog_id), "Progression") + self.timestamp.strftime("%d-%m-%Y") + ".xml"
        if not path.exists('progressions'):
            mkdir('progressions')
        xml_file = open('progressions/{}'.format(filename), 'w')
        xml_file.write(export_data)
        xml_file.close()

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

    def load_progression(self):
        # TODO: Fix this.
        prog = GUI.load_file()
        tree = et.parse(prog)
        root = tree.getroot()
        cnv = root[0].text
        for i in cnv:
            self.chords.append(i)

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

    def __init__(self, func, chords, exp_func=None):
        """
        :param func: This is the main function that is passed in.
        :param chords: Initially empty list. When the GUI window is initiated, the contents of this list become
        :param exp_func: Initialised with None. Later in the main script, None is replaced with 'export_progression()"
        from the Progression class.
        identical to the contents of the variable 'chords_playing' in the class 'Progression'.
        """

        tk.Tk.__init__(self)
        GUI.title(self, "Text To Music")
        self.func = func
        self.exp_func = exp_func
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
        self.load_prog_button = tk.Button(self.input_frame, text="Load Progression", command=self.load_file)
        self.load_prog_button.grid(row=0, column=3, padx=5)
        self.chord_title = tk.Label(self.output_frame, text="Chords in this progression: ")
        self.chord_title.grid(row=0, column=0)
        self.chords_display = tk.Text(self.output_frame, height=2, width=40)
        self.chords_display.grid(row=1, column=0)
        self.scrollbar = tk.Scrollbar(self.output_frame)
        self.scrollbar.grid(row=1, column=2)
        self.chords_display.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.chords_display.yview)
        self.export_prog_button = tk.Button(self.output_frame, text="Export Progression",
                                            command=exp_func, state="disabled")
        self.export_prog_button.grid(row=2, column=0, pady=5)
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

        self.chords.append("/")
        self.chords_display.insert(tk.END, self.chords)

    def prog_button_status(self, arg):
        """
        This method either disables or enables 'self.play_prog_button' depending on the argument passed.
        :param arg: Value is either 0 or 1. 0 makes the method disable 'self.play_prog_button', 1 enables it.
        """

        if arg == 0:
            self.play_prog_button.config(state="disabled")
        elif arg == 1:
            self.play_prog_button.config(state="normal")

    def export_button_status(self, arg):
        """
        This method either disables or enables 'self.export_prog_button' depending on the argument passed.
        :param arg: Value is either 0 or 1. 0 makes the method disable 'self.play_prog_button', 1 enables it.
        """

        if arg == 0:
            self.export_prog_button.config(state="disabled")
        elif arg == 1:
            self.export_prog_button.config(state="normal")

    @staticmethod
    def load_file():
        file = tk.filedialog.askopenfilename(filetypes=(("XML Files", '*.xml'), ("All Files", '*.*')))
        return file


