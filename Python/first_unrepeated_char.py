# Given a string s, find the first unrepeated char in the string
# if there are no repeated chars, return none

def firstUnrepeatedChar(s):
    charFreq = {}

    for char in s:
        if char in charFreq:
            charFreq[char] += 1
        else:
            charFreq[char] = 1

    # print(charFreq)

    for char in s:
        if charFreq[char] == 1:
            return char
        
    return None

print(firstUnrepeatedChar('hello'))
print(firstUnrepeatedChar('mmississipi'))
print(firstUnrepeatedChar('noonee'))
