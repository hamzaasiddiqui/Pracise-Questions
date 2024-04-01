# ArrayChallenge(strArr) tak the array of strings stored in strArr, 
# which will only contain two strings of equal length and 
# return the number of characters at each position that are 
# different between them. For example: if strarr is [house", "hours"] 
# then your program should return 2. The string will always be of 
# equal length and will only contain lowercase characters from the 
# alphabet and numbers. 6 7 8 9 fur / } // k conse 
# Examples Input: [*10011", "10100"] Output: 3 Input: ("abcdef", "defabc"l Output: 6


def different_chars(arr1, arr2):
    j = 0
    count = 0
    for char in arr1:
        if char != arr2[j]:
            count += 1
        j += 1

    return count

c = different_chars('house', 'hours')

print(c)

c = different_chars('10011', '10100')

print(c)

c = different_chars('abcdef', 'defabc')

print(c)