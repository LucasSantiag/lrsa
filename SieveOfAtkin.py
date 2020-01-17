import math

class SieveOfAtkin:
    def __init__(self, bits):
        self.bits = bits / 2
        self.primes = [2, 3, 5]

    def _getSieve():
        if ((self.bits & (n-1) == 0) and (self.bits > 0)):
            return -1
        else:
            nDigits = len(int(''.join(['1'] * self.bits)))
            minimalNum = int(''.join((['0'] * nDigits - 1).insert(0, '1'))
            maximunNum = int(['9'] * nDigits)
            return list(range(minimalNum, maximunNum))

    def generatePrimes():
        listOfNums = _getSieve
        if(listOfNums == -1):
            print("Number of bits must be power of two.")
        else:
            nNums = len(listOfNums)
            boolList = [False] * nNums

            for x in listOfNums:
                for y in listOfNums:
                    n = (4 * x * x) + (y * y)

