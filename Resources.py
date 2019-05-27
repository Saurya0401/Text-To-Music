import tkinter as tk
import threading
import random
import playsound
import lxml.etree as et
from os import path, mkdir
from datetime import datetime


class Progression:
    """
    This class contains all the methods and relevant variables needed to generate and manage chord progressions.
    Note: 'CNV/cnv' is an abbreviation for Chord-Number Value, an integer corresponding to a specific chord.
    """

    # Dictionary containing all possible chord progressions. Each key is the cnv of the progression's first chord.
    extension_dict = {1: [1, 8, 22, 6], 2: [2, 7, 2, 23], 3: [3, 10, 24, 19], 4: [4, 11, 13, 9], 5: [5, 24, 14, 10],
                      6: [6, 1, 15, 22], 7: [7, 2, 15, 12], 8: [8, 3, 17, 24], 9: [9, 4, 18, 2],
                      10: [10, 5, 19, 3], 11: [11, 4, 6, 8], 12: [12, 7, 20, 5], 13: [13, 9, 4, 11],
                      14: [14, 19, 5, 10], 15: [15, 11, 6, 1], 16: [16, 11, 12, 2, 9], 17: [17, 1, 8, 3],
                      18: [18, 2, 9, 4], 19: [19, 3, 10, 5], 20: [20, 4, 11, 6], 21: [21, 16, 5, 14], 22: [22, 6, 1, 8],
                      23: [23, 7, 2, 9], 24: [24, 8, 3, 10]}

    # Dictionary used to convert cnvs to chords.
    cnv_dict = {1: "A", 2: "A#", 3: "B", 4: "C", 5: "C#", 6: "D", 7: "D#", 8: "E", 9: "F", 10: "F#", 11: "G",
                12: "G#", 13: "Am", 14: "A#m", 15: "Bm", 16: "Cm", 17: "C#m", 18: "Dm", 19: "D#m", 20: "Em",
                21: "Fm", 22: "F#m", 23: "Gm", 24: "G#m"}

    def __init__(self, phrase=None):
        """
        :param phrase: the phrase inputted by the user
        """
        self.phrase = phrase
        self.characters = []
        self.cnv_progression = []
        self.chord_progression = []

    def clear_cnvs_chords(self):
        self.chord_progression.clear()
        self.cnv_progression.clear()

    def create_inputs(self):
        """
        Deletes existing lists chords and cnvs, then creates new lists of both.
        """

        self.clear_cnvs_chords()
        self.characters = [i for i in self.phrase if i not in (" ", ",", ".")]
        self.cnv_progression = self.extension_dict[random.randint(1, 24)]
        self.chord_progression = []

    def edit_progression(self):
        """
        Deletes excess characters or cnvs.
        """

        if len(self.characters) < len(self.cnv_progression):
            del self.cnv_progression[len(self.characters):]
        elif len(self.characters) > len(self.cnv_progression):
            cnv_deficit = len(self.characters) - len(self.cnv_progression)
            self.cnv_progression.extend([random.choice(self.cnv_progression) for _ in range(cnv_deficit)])
        return self.to_chords()

    def to_chords(self):
        """
        Converts cnvs to chords.
        :return: a list containing the initial list of cnvs, a list of converted chords and errors.
        """

        err_list = []
        for cnv in self.cnv_progression:
            if cnv in Progression.cnv_dict.keys():
                self.chord_progression.append(Progression.cnv_dict[cnv])
            else:
                err_list.append(cnv)
        return [self.chord_progression, err_list]

    def play_progression(self):
        serial_number = [i for i in range(47845, 47869)]
        chord_number = [i for i in range(1, 25)]
        for i in self.cnv_progression:
            try:
                filename = "audio files/{}__{}.wav".format(serial_number[i - 1], chord_number[i - 1])
                playsound.playsound(filename)
            except playsound.PlaysoundException:
                print('Error: audio files not found.')

    def export_progression(self):
        """
        This method exports the chords and cnvs in the current progression in an XML file.
        """

        root = et.Element('progression')
        timestamp = et.SubElement(root, 'timestamp')
        timestamp.text = str(datetime.now())
        cnv = et.SubElement(root, 'CNV')
        cnv.text = " ".join(str(i) for i in self.cnv_progression)
        chords = et.SubElement(root, 'chords')
        chords.text = " ".join(i for i in self.chord_progression if i != "/")
        export = et.tostring(root, encoding='unicode', pretty_print=True)
        progression_id = [self.chord_progression[0], "_prog_", datetime.now().strftime("%d-%m-%Y")]
        filename = "{}".format("".join(str(i) for i in progression_id)) + ".xml"
        if not path.exists('progressions'):
            mkdir('progressions')
        xml_file = open('progressions/{}'.format(filename), 'w')
        xml_file.write(export)
        return xml_file.close()


class GUI(tk.Tk):
    """
    This class contains the methods needed to display and control the GUI window using tkinter.
    """

    def __init__(self, play_func, exp_func, title="Text to Music", min_width=400, min_height=200):
        """
        :param play_func: Function that plays the progression (play_prog() from TextToMusic.py)
        :param exp_func: Function that exports the progression (export_prog() from TextToMusic.py)
        :param title: Title of the GUI window
        :param min_width: Default (and currently fixed) width of the window
        :param min_height: Default (and currently fixed) height of the window
        """

        # defining main window properties
        tk.Tk.__init__(self)
        GUI.title(self, title)
        GUI.geometry(self, "%dx%d" % (min_width, min_height))
        GUI.resizable(self, width=False, height=False)
        GUI.grid_rowconfigure(self, (0, 3), weight=1)
        GUI.grid_columnconfigure(self, (0, 2), weight=1)

        # defining external functions
        self.play_func = play_func
        self.exp_func = exp_func

        # defining GUI components
        self.input_frame = tk.Frame(self)
        self.output_frame = tk.Frame(self)
        self.phrase = tk.StringVar()
        self.phrase_input_label = tk.Label(self.input_frame, text="Enter phrase: ")
        self.phrase_input = tk.Entry(self.input_frame, textvariable=self.phrase)
        self.play_prog_button = tk.Button(self.input_frame, text="Play Progression!", command=self.play_prog, bg="blue",
                                          fg="white")
        self.export_prog_button = tk.Button(self.input_frame, text="Export Progression!", command=self.export_prog,
                                            state='disabled')
        self.chord_display_label = tk.Label(self.output_frame, text="Chords in this progression: ")
        self.chords_display = tk.Label(self.output_frame)
        self.info = tk.Label(self.output_frame)

    def display_window(self):
        """
        Show gui window with placed widgets.
        """

        self.input_frame.grid({'row': 1, 'column': 1, 'sticky': 'nsew'})
        self.output_frame.grid({'row': 2, 'column': 1, 'sticky': 'nsew'})
        self.input_frame.grid_columnconfigure((0, 3), weight=1)
        self.output_frame.grid_columnconfigure((0, 3), weight=1)
        self.rearrange_widgets({self.phrase_input_label: {'row': 1, 'column': 1, 'pady': 5},
                                self.phrase_input: {'row': 1, 'column': 2, 'pady': 5},
                                self.play_prog_button: {'row': 2, 'column': 1, 'pady': 5},
                                self.export_prog_button: {'row': 2, 'column': 2, 'pady': 5},
                                self.chord_display_label: {'row': 1, 'column': 1, 'pady': 10},
                                self.chords_display: {'row': 2, 'column': 1},
                                self.info: {'row': 3, 'column': 1}})

    def play_prog(self):
        """
        Creates a thread whose target is self.play_func and joins the thread if it is already running.
        :return: Start the thread.
        """
        self.play_prog_button.config(state='disabled')
        play_thread = threading.Thread(target=self.play_func, daemon=True)
        if not play_thread.is_alive():
            self.chords_display.config(text="")
            return play_thread.start()

    def export_prog(self):
        """
        Creates a thread whose target is self.export_func and joins the thread if it is already running.
        :return: Start the thread.
        """
        self.export_prog_button.config(state='disabled')
        export_thread = threading.Thread(target=self.exp_func)
        if export_thread.is_alive():
            export_thread.join()
        return export_thread.start()

    @staticmethod
    def rearrange_widgets(widgets_properties):
        """
        Modifies the shape and placement of multiple widgets.
        :param widgets_properties: A dictionary containing widgets and their properties.
        """

        for widget, properties in widgets_properties.items():
            widget.grid(cnf=properties)
