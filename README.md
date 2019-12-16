# Oracle and Detective

## Origin

This is a programming problem posed to me by a friend. I'm not sure the true origin or the proper name. I've made up the Oracle and Detective characters.

## Problem Statement

An Oracle is thinking of two positive integers and a Detective must guess them. Every time the Detective guesses incorrectly the Oracle will increase the second number by the first number.

### Iteration rule:
- $$$ A_0 = a $$$
- $$$ B_0 = b $$$
- $$$ A_n = A_{n-1} + B_{n-1} $$$
- $$$ B_n = B_{n-1} $$$

### Example:
- Oracle thinks of 1 and 5
- Detective guesses 2 and 2
- Oracle is now thinking of 6 and 5
- Detective guesses 1 and 5
- Oracle is now thinking of 11 and 5
- Detective guesses 11 and 5
- Detective wins

The Detective is given unlimited guesses. What strategy should the Detective use to guess the Oracle's numbers with 100% certainty?

### Solution:
Search through all possible combinations of the two numbers. Use a diagonal search so that every pair from (0, 0) to (inf, inf) is tried eventually. At every guess, the Detective can calculate the expected current numbers the Oracle would be thinking of if some guess were true. For example if the Oracle started out thinking of 4 and 5, then after 2 iterations the Oracle would be thinking of 14 and 5 (4 + 5 * 2 = 14).

### Expected Guesses:
If the Oracle chooses numbers between 0 and 100 it will take up to 20000 attempts for the Detective to guess correctly, but the Detective will eventually get the combination correct.