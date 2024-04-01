def remove_duplicate(input_list):
    unique_vals = []

    for value in input_list:
        if value not in unique_vals:
            unique_vals.append(value)

    return unique_vals


duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
print(duplicates)
uniques  = remove_duplicate(duplicates)
print(uniques)