# Sets: unordered, mutable, no duplicates
myset = set("hello")


myset.add(2)
myset.add(3)

for i in myset:
    print(i)

print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = (2, 3, 5, 7)

union = odds.union(evens)
print(union)

i = odds.intersection(evens)

print(i)

intersect = odds.intersection(primes)
print(intersect)

diff = odds.difference(primes)
print(diff)


symdiff = odds.symmetric_difference(primes)
print(symdiff)


setA = {1, 2, 3, 4}
setB = {1, 2, 3}
setC = {8, 24, 342}

print(setA.issuperset(setB))

print(setA.isdisjoint(setC))


a = frozenset([1, 2, 3, 4])

print(a)
