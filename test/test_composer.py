from unittest import TestCase
import mingus.extra.lilypond as lilypond

from Composer import Composer


class TestComposer(TestCase):

    def test_triad_251(self):
        composer = Composer()
        composition = composer.compose(None)
        self.assertIsNotNone(composition)
        track = composition.tracks[0]
