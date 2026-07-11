from math import factorial

def recursive_counter():

    calls = 0

    def fact(n):
        nonlocal calls
        calls += n

        fact.calls = calls

        return factorial(n)

    return fact


# fact = recursive_counter()
# print(fact(4))      # -> 24
# print(fact.calls)   # -> 4

f = recursive_counter()
f(3)
print(f.calls)
f(2)
print(f.calls)