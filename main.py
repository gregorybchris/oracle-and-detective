"""The oracle and the detective simulation."""
import argparse

from colorama import init as color_init, Fore

from detective import Detective
from oracle import Oracle


def run_simulation(alpha_range, delta_range, n_guesses, verbose=False):
    """Run one simulation."""
    oracle = Oracle(alpha_range, delta_range)

    detective = Detective()
    if verbose:
        print(Fore.BLUE + f"\n\nAttempting {n_guesses} guesses...")
    result = detective.search(oracle, n_guesses)

    if result is None:
        alpha_0, delta = oracle.get_secrets()
        if verbose:
            print(Fore.RED + "The detective failed :(")
            print(Fore.RED + f"The oracle was initially thinking of alpha={alpha_0}, delta={delta}")
    else:
        guess, alpha_0, delta, alpha_n = result
        if verbose:
            print(Fore.GREEN + f"Discovered the oracle's secrets after {guess} guesses!")
            print(Fore.GREEN + f"alpha_0={alpha_0}, delta={delta}, alpha_n={alpha_n}")

    return result is not None, alpha_0, delta


def run_simulations(n_simulations, verbose, alpha_range, delta_range, n_guesses):
    """Run many simulations."""
    n_successes = 0
    for simulation in range(n_simulations):
        print(f"Simulation #{simulation + 1}", end='\r')
        result, _, _ = run_simulation(alpha_range, delta_range, n_guesses, verbose=verbose)
        if result:
            n_successes += 1
    print(f"\nSuccessful simulations: {n_successes}/{n_simulations}")


def parse_args():
    """Parse arguments to the script."""
    parser = argparse.ArgumentParser(description="Oracle and detective" "simulation.")
    parser.add_argument('--n_simulations', type=int, default=1,
                        help="Number of simulations to perform")
    parser.add_argument('--verbose', default=True, action='store_true',
                        help="Whether to print each simulation step.")
    parser.add_argument('--alpha_range', type=int, nargs=2, default=(0, 100),
                        help="Range of the oracle's alpha number")
    parser.add_argument('--delta_range', type=int, nargs=2, default=(0, 100),
                        help="Range of the oracle's delta number")
    parser.add_argument('--n_guesses', type=int, default=10000,
                        help="Number of guesses the detective is allowed.")

    return parser.parse_args()


if __name__ == '__main__':
    color_init(autoreset=True)
    args = parse_args()
    run_simulations(args.n_simulations, args.verbose, args.alpha_range, args.delta_range, args.n_guesses)
