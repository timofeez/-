def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def primorial(n):
    counter = 0
    cur_num = 0
    mult = 1
    while True:
        cur_num += 1
        if (is_prime(cur_num)):
            mult *= cur_num
            counter += 1
        if counter == n:
            return mult

def translator(num: list) -> int:
    return sum((digit * primorial(i + 1) for i, digit in enumerate(num[::-1])))

#tester = [int(i) for i in "0:0:6:3:0:1".split(":")]
#print(translator(tester))

cur_max = float("-inf")
indices = []

for i in range(int(input())):
    number = translator([int(i) for i in input().split(":")])
    if number > cur_max:
        indices = []
        cur_max = number
        indices.append(i + 1)
    elif number == cur_max:
        indices.append(i + 1)
print(*indices, sep="\n")