import sys
from fractions import Fraction


def determinant(a):
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if a[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        det *= a[col][col]
        for row in range(col + 1, n):
            factor = a[row][col] / a[col][col]
            for k in range(col, n):
                a[row][k] -= factor * a[col][k]
    return det


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(filename) as f:
        tokens = f.read().split()
    n = int(tokens[0])
    numbers = [Fraction(t) for t in tokens[1:1 + n * n]]
    matrix = [numbers[i * n:(i + 1) * n] for i in range(n)]
    det = determinant(matrix)
    if det.denominator == 1:
        print(det.numerator)
    else:
        print(float(det))


if __name__ == "__main__":
    main()
