import random

from mingus.containers import Bar, Composition, Track
import mingus.core.chords as Chords

from Exercise import Exercise

inversions = [lambda c: c, Chords.first_inversion, Chords.second_inversion]


class TriadExercise251(Exercise):
    def __init__(self):
        Exercise.__init__(self)

    def compose(self, context):
        key = 'Gb'
        bar = Bar()
        track = Track()
        track + bar
        composition = Composition()
        composition + track

        for degree in [Chords.II, Chords.V, Chords.I]:
            chord = degree(key)
            inversion = random.choice(inversions)(chord)
            bar + inversion

        return composition
