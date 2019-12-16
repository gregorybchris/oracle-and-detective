import diagonal_search


class Detective:
    def __init__(self, verbose=False):
        self._verbose = verbose

    def search(self, oracle, n_guesses):
        oracle.reset()
        for guess in range(n_guesses):
            alpha_0, delta = diagonal_search.get_countable_indexes(guess)
            alpha_n = alpha_0 + guess * delta

            if self._verbose:
                print(f"Attempt {guess}: a_0={alpha_0}, da={delta}, a_n={alpha_n}")

            guess_result = oracle.ask(alpha_n, delta)
            if guess_result:
                return guess, alpha_0, delta, alpha_n
        return None
