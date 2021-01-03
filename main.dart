import 'detective.dart';
import 'oracle.dart';

runSimulation(nGuesses) {
  print("~Oracle and Detective~");
  Oracle oracle = Oracle(0, 100, 0, 100);
  Detective detective = Detective(verbose: false);

  print("Attempting $nGuesses guesses...");

  DetectiveResult result = detective.search(oracle, nGuesses);

  if (result == null) {
    OracleSecrets trueSecrets = oracle.getSecrets();
    int alphaSecret = trueSecrets.alpha;
    int deltaSecret = trueSecrets.delta;
    print("The detective failed :(");
    print("The oracle was initially thinking of alpha=$alphaSecret, delta=$deltaSecret");

  }
  else {
    int guess = result.nGuesses;
    int alphaFinal = result.alphaFinal;
    int alphaSecret = result.alphaSecret;
    int deltaSecret = result.deltaSecret;
    print("Discovered the oracle's secrets after $guess guesses!");
    print("a0=$alphaSecret, da=$deltaSecret, an=$alphaFinal");
  }
}

main() {
  runSimulation(10000);
}