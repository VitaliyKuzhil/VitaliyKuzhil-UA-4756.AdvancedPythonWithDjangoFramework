def divisor(n):

    for i in range(1, n + 1):
        if n % i == 0:
            yield i
            
    while True:
        yield None


three = divisor(3)
print(next(three)) # => 1
print(next(three)) # => 3
print(next(three)) # => None