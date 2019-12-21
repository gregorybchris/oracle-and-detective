import 'dart:math';

int _getDiagonalIndex(n) {
  return (sqrt(.25 + 2 * n) + .5).toInt() - 1;
}

int _getDiagonalNumber(index) {
  return index * (index + 1) ~/ 2;
}

DiagonalIndices getCountableIndexes(iteration) {
  int diagonalIndex = _getDiagonalIndex(iteration);
  int diagonalNumber = _getDiagonalNumber(diagonalIndex);

  int v1 = iteration - diagonalNumber;
  int v2 = diagonalIndex - v1;

  return DiagonalIndices(v1, v2);
}

class DiagonalIndices {
  int v1, v2;

  DiagonalIndices(this.v1, this.v2) {}
}