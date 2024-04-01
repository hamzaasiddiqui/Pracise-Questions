def lru(strArr):
    cache = []
    cacheSize = 5

    for char in strArr:
        if char in cache:
            cache.remove(char)
        elif len(cache) >= cacheSize:
            cache.pop(0)

        cache.append(char)

    return '-'.join(cache)

print(lru(['A', 'B', 'C', 'D', 'A', 'E', 'D', 'Z']))