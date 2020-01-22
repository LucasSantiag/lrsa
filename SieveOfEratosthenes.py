import math

class SieveOfEratosthenes:
    def __init__(self, bits):
        self.bits = bits / 2
        self.primes = [2, 3, 5]

    def getSieve(self, bits):
        if ((bits & (bits-1) != 0) or (bits < 0)):
            return -1
        else:
            nDigits = len(''.join(['1'] * self.bits))
            minimalNum = int(''.join((['0'] * nDigits - 1).insert(0, '1')))
            maximumNum = int(['9'] * nDigits)
            return list(range(minimalNum, maximunNum))

    def generatePrimes(self):
	srange = self.getSieve(self.bits)
        prime_list = []
        for i in srange:
            if i not in prime_list:
                print (i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)


