import random

def randomWord(collection):
    if collection:
        
        for item in collection:
            yield item

        while True:
            yield random.choice(collection)

    yield None


list = ['book', 'apple', 'word']

books = randomWord(list)

# then possible output example 

print(next(books)) # returns apple
print(next(books)) # returns book
print(next(books)) # returns word
print(next(books)) # returns book