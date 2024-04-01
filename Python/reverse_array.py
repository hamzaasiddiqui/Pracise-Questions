# Reverse array

# def reverseArray(arr):
#     arr = arr[::-1]
#     return arr

def reverseArray(arr):
    j = len(arr) - 1

    for i in range(len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        j -= 1

    return None

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
reverseArray(arr)
print(arr)
