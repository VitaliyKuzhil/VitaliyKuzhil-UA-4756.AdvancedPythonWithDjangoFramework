def limited_cache(limit):
    
    caches = dict()

    def cache(key, value=None):

        if value and len(caches) == limit:
            
            if key not in caches.keys():
                del caches[next(iter(caches))]
            else:
                del caches[key]

        if key and value:
            caches[key] = value

        return None if key not in caches.keys() else caches[key]

    return cache

# cache = limited_cache(2)

# cache('a', 1)
# cache('b', 2)

# print(cache('a'))  # -> 1

# cache('c', 3)

# print(cache('a'))  # -> None (removed)


cache = limited_cache(3)
cache("x", 1)
cache("y", 2)
cache("m", 3)
cache("n", 4)
cache("m", 33)
print(cache("x"))
print(cache("y"))
print(cache("m"))
print(cache("n"))
