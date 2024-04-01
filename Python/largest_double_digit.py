# Have the function MathChallenge (num) take the num parameter being passed 
# and determine the largest double digit number within the whole number. 
# For example: if num is 4759472 then your program should return 94 
# because that is the largest double digit number. The input always contain
# at least two positive digits. 
# Examples Input: 453857 Output: 85 Input: 363223311 Output: 63


def largestDoubleDigit(num):
    numStr = str(num)

    largestDoubleDigit = int(numStr[:2])

    for i in range(len(numStr) - 1):
        currentDoubleDigit = int(numStr[i:i+2])

        if currentDoubleDigit > largestDoubleDigit:
            largestDoubleDigit = currentDoubleDigit

    return largestDoubleDigit

print(largestDoubleDigit(453857))
print(largestDoubleDigit(363223311))