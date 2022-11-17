from itertools import permutations
from fractions import Fraction

def get_answer(cp: tuple) -> int:
    return (cp[0] / cp[1] + cp[2] / cp[3] + cp[4] / cp[5] + cp[6] / cp[7])
numbers = [int(i) for i in input().split()]
result = float("inf")
for permutation in permutations(numbers, r=8):
    result = min(get_answer(permutation), result)
x = Fraction(result)
print(x.numerator, x.denominator)