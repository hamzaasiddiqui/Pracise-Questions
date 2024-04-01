def count_strings(strs):
    counts = {}
    for s in strs:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts

# Example usage
strs = ["apple", "banana", "apple", "cherry", "banana", "cherry", "cherry"]
print(count_strings(strs))