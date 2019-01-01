class Progressions:
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

    def add_chords(self):
        self.chords.extend(self.extra)


class A(Progressions):

    first_chords = [1, 13]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def AEFSmD_progression(self):
        if self.first_chord in A.first_chords and self.first_chord == 1:
            self.chords.extend([8, 22, 6])
        return self.chords

    def AmFCG_progression(self):
        if self.first_chord in A.first_chords and self.first_chord == 13:
            self.chords.extend([9, 4, 11])
        return self.chords


class AS(Progressions):

    first_chords = [2, 14]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def ASDSASGm_progression(self):
        if self.first_chord in AS.first_chords and self.first_chord == 2:
            self.chords.extend([7, 2, 23])
        return self.chords

    def ASmDSmCSFS_progression(self):
        if self.first_chord in AS.first_chords and self.first_chord == 14:
            self.chords.extend([19, 5, 10])
        return self.chords


class B(Progressions):

    first_chords = [3, 15]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def BFSGSmDSmEBEFSm_progression(self):
        if self.first_chord in B.first_chords and self.first_chord == 3:
            self.chords.extend([10, 24, 19, 8, 3, 8, 22])
        return self.chords

    def BmGDA_progression(self):
        if self.first_chord in B.first_chords and self.first_chord == 15:
            self.chords.extend([11, 6, 1])
        return self.chords


class C(Progressions):

    first_chords = [4, 16]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def CGAmF_progression(self):
        if self.first_chord in C.first_chords and self.first_chord == 4:
            self.chords.extend([11, 13, 9])
        return self.chords

    def CmGmGSDSFmCmFmGm_progression(self):
        if self.first_chord in C.first_chords and self.first_chord == 16:
            self.chords.extend([11, 12, 2, 9, 16, 9, 11])
        return self.chords


class CS(Progressions):

    first_chords = [5, 17]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def CSGSASmFS_progression(self):
        if self.first_chord in CS.first_chords and self.first_chord == 5:
            self.chords.extend([24, 14, 10])
        return self.chords

    def CSmAEB_progression(self):
        if self.first_chord in CS.first_chords and self.first_chord == 17:
            self.chords.extend([1, 8, 3])
        return self.chords


class D(Progressions):

    first_chords = [6, 18]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def DABmFSmGDGA_progression(self):
        if self.first_chord in D.first_chords and self.first_chord == 6:
            self.chords.extend([1, 15, 22, 11, 6, 11, 1])
        return self.chords

    def DmASFC_progression(self):
        if self.first_chord in D.first_chords and self.first_chord == 18:
            self.chords.extend([2, 9, 4])
        return self.chords


class DS(Progressions):

    first_chords = [7, 19]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def DSASBmGS_progression(self):
        if self.first_chord in DS.first_chords and self.first_chord == 7:
            self.chords.extend([2, 15, 12])
        return self.chords

    def DSmBFSCS_progression(self):
        if self.first_chord in DS.first_chords and self.first_chord == 19:
            self.chords.extend([3, 10, 5])
        return self.chords


class E(Progressions):

    first_chords = [8, 20]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def EBCSmGSmAEAB_progression(self):
        if self.first_chord in E.first_chords and self.first_chord == 8:
            self.chords.extend([3, 17, 24, 1, 8, 1, 3])
        return self.chords

    def EmCGD_progression(self):
        if self.first_chord in E.first_chords and self.first_chord == 20:
            self.chords.extend([4, 11, 6])
        return self.chords


class F(Progressions):

    first_chords = [9, 21]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def FCDmAS_progression(self):
        if self.first_chord in F.first_chords and self.first_chord == 9:
            self.chords.extend([4, 18, 2])
        return self.chords

    def FmCmCSASm_progression(self):
        if self.first_chord in F.first_chords and self.first_chord == 21:
            self.chords.extend([16, 5, 14])
        return self.chords


class FS(Progressions):

    first_chords = [10, 22]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def FSCSDSmB_progression(self):
        if self.first_chord in FS.first_chords and self.first_chord == 10:
            self.chords.extend([5, 19, 3])
        return self.chords

    def FSmDAE_progression(self):
        if self.first_chord in FS.first_chords and self.first_chord == 22:
            self.chords.extend([6, 1, 8])
        return self.chords


class G(Progressions):

    first_chords = [11, 23]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def GCDE_progression(self):
        if self.first_chord in G.first_chords and self.first_chord == 11:
            self.chords.extend([4, 6, 8])
        return self.chords

    def GmDSASF_progression(self):
        if self.first_chord in G.first_chords and self.first_chord == 23:
            self.chords.extend([7, 2, 9])
        return self.chords


class GS(Progressions):

    first_chords = [12, 24]

    def __init__(self, first_chord, chords):
        super().__init__(first_chord, chords)

    def GSDSEmCS_progression(self):
        if self.first_chord in GS.first_chords and self.first_chord == 12:
            self.chords.extend([7, 20, 5])
        return self.chords

    def GSmEBFS_progression(self):
        if self.first_chord in GS.first_chords and self.first_chord == 24:
            self.chords.extend([8, 3, 10])
        return self.chords
