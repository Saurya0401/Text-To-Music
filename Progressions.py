class Progressions:

    first_chords = [int(i) for i in range(1, 25)]

    extension_dict = {1: [8, 22, 6], 2: [7, 2, 23], 3: [10, 24, 19, 8, 3, 8, 22], 4: [11, 13, 9], 5: [24, 14, 10],
                      6: [1, 15, 22, 11, 6, 11, 1], 7: [2, 15, 12], 8: [3, 17, 24, 1, 8, 1, 3], 9: [4, 18, 2],
                      10: [5, 19, 3], 11: [4, 6, 8], 12: [7, 20, 5], 13: [9, 4, 11], 14: [19, 5, 10], 15: [11, 6, 1],
                      16: [11, 12, 2, 9, 16, 9, 11], 17: [1, 8, 3], 18: [2, 9, 4], 19: [3, 10, 5], 20: [4, 11, 6],
                      21: [16, 5, 14], 22: [6, 1, 8], 23: [7, 2, 9], 24: [8, 3, 10]}

    def __init__(self, first_chord, chords=None, extra=None):
        self.first_chord = first_chord
        if chords is None:
            self.chords = []
        else:
            self.chords = chords
        if extra is None:
            self.extra = []
        else:
            self.extra = extra

    def generate_progression(self):
        if self.first_chord in Progressions.first_chords:
            self.chords.extend(Progressions.extension_dict[self.first_chord])
        return self.chords

    def add_chords(self):
        self.chords.extend(self.extra)