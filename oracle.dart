import 'dart:math';

class Oracle {
  int alphaCurrent, alphaSecret, deltaSecret;

  Oracle(alphaMin, alphaMax, deltaMin, deltaMax) {
    var rng = new Random();
    this.alphaSecret = rng.nextInt(alphaMax) + alphaMin;
    this.alphaCurrent = this.alphaSecret;
    this.deltaSecret = rng.nextInt(deltaMax) + deltaMin;
  }

  bool ask(int alpha, int delta) {
    if (alpha == this.alphaCurrent && delta == this.deltaSecret)
      return true;

    this.alphaCurrent += this.deltaSecret;
    return false;
  }

  void reset() {
    this.alphaCurrent = this.alphaSecret;
  }

  OracleSecrets getSecrets() {
    return OracleSecrets(this.alphaSecret, this.deltaSecret);
  }
}

class OracleSecrets {
  int alpha, delta;

  OracleSecrets(this.alpha, this.delta) {}
}