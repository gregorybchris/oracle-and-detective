import random


class Oracle:
    def __init__(self, alpha_range, delta_range):
        self._alpha_n = random.randint(*alpha_range)
        self._alpha_0 = self._alpha_n
        self._delta = random.randint(*delta_range)

    def ask(self, alpha, delta):
        if alpha == self._alpha_n and delta == self._delta:
            return True

        self._alpha_n += self._delta
        return False

    def reset(self):
        self._alpha_n = self._alpha_0

    def get_secrets(self):
        return self._alpha_0, self._delta
