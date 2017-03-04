import itertools as it


class Primes:
    @staticmethod
    def primeFactors(number):
        er = Primes.eryst()
        score = ""
        while number != 1:
            p = er.next()
            ctr = 0
            while number % p == 0:
                number /= p
                ctr += 1
            if ctr == 1:
                score += "({})".format(p)
            if ctr > 1:
                score += "({}**{})".format(p, ctr)
        return score

    @staticmethod
    def first(x):
        er = Primes.eryst()
        return [er.next() for z in range(x)]

    @staticmethod
    def eryst():
        D = {}
        yield 2
        for q in it.islice(it.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q * q] = q
                yield q
            else:
                x = q + p
                while x in D or not (x & 1):
                    x += p
                D[x] = p

                # @staticmethod
                # def first_2(ammount):
                #     firsts = {}
                #     return [firsts.setdefault(i, i) for i in range(2, ammount)
                #             if 0 not in [for]]


if __name__ == '__main__':
    print Primes.primeFactors(10)
