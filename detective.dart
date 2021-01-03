import 'diagonalize.dart';
import 'oracle.dart';

class Detective {
  bool verbose;

  Detective({this.verbose:false}) {}

  DetectiveResult search(Oracle oracle, int nGuesses) {
    oracle.reset();
    for (int guess = 0; guess < nGuesses; guess++) {
      DiagonalIndices indices = getCountableIndexes(guess);
      int alphaSecret = indices.v1;
      int deltaSecret = indices.v2;
      int alphaGuess = alphaSecret + guess * deltaSecret;

      if (this.verbose)
        print("Attempt $guess: a0=$alphaSecret, da=$deltaSecret, an=$alphaGuess");
      
      bool guessCorrect = oracle.ask(alphaGuess, deltaSecret);
      if (guessCorrect)
        return DetectiveResult(guess, alphaGuess, alphaSecret, deltaSecret);
    }

    return null;
  }
}

class DetectiveResult {
  int nGuesses, alphaFinal, alphaSecret, deltaSecret;

  DetectiveResult(this.nGuesses, this.alphaFinal, this.alphaSecret, this.deltaSecret) {}
}