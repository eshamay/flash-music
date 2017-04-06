from TriadExercise251 import TriadExercise251


class Composer:
    def __init__(self):
        self.exercise = TriadExercise251()

    def compose(self, context):
        return self.exercise.compose(context)
