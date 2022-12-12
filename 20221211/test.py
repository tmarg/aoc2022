from collections import defaultdict

def primeFactors(number):
    originalNumber = number
    factors = defaultdict(int)
    i = 2
    while i <= number // 2:
        while number % i == 0:
            factors[i] += 1
            number = number / i
        i += 1
    if number != 1:
        factors[int(number)] = 1
    return factors

print(primeFactors(77))
print(primeFactors(100000))
print(primeFactors(87))
print(primeFactors(103131113123))
print(41*271*1087*8539)
print(103131113123)