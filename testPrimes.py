import csv
import unittest

  # Todos os primos > 3 possuem a forma 6n ± 1
  # primos inferiores a ou iguais a 3 => 2,3
  # Testar para 2, testar para 3 (edge cases)
  # testar para os primeiros 10000 numeros (excepto 2 e 3 cases) com base num dataset de primos
  # testei uma função com o mesmo propósito feita por mim para termo de comparação e sanidade

class TestPrimes(unittest.TestCase):

    def testIsPrimeTwo(self):
        self.assertEqual(primes(3), [False, False, True])

    def testIsPrimeThree(self):
        self.assertEqual(primes(4), [False, False, True, True])

    def testIsPrimeAfterThree(self):
        primesArr = [False] * 1010

        with open('P-100000.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                primesArr[int(row[1])] = True

        for n in range(5,len(primesArr)):
            self.assertEqual(primes(n), primesArr[:n])


    def testIsGoodPrimeTwo(self):
        self.assertEqual(goodPrimes(3), [False, False, True])

    def testIsGoodPrimeThree(self):
        self.assertEqual(goodPrimes(4), [False, False, True, True])

    def testIsGoodPrimeAfterThree(self):
        primesArr = [False] * 1010

        with open('P-1000.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                primesArr[int(row[1])] = True

        primesArr[2] = True
        primesArr[3] = True
        for n in range(2,len(primesArr)):
            self.assertEqual(goodPrimes(n), primesArr[:n])


def primes(n):
    return [(lambda x: [(x % i) == 0 for i in range(2, x)].count(True)
         == 2)(n) for n in range(1, n + 1)]

def checkPrimes(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

def goodPrimes(n):
    primesArr = [False] * (n)
    for i in range(0,n):
        primesArr[i] = checkPrimes(i)
    
    return primesArr

def main():
    unittest.main()


if __name__ == "__main__":
    main()