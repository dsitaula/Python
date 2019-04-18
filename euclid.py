def findGcd (firstNumber, secondNumber):
    while(secondNumber != 0):
        temp = firstNumber
        firstNumber = secondNumber
        secondNumber = temp % secondNumber
    return firstNumber

print (findGcd(50, 20))
