from collections import Counter
import math

dictPossiblePoints = {10: 2, 8: 2, 5: 1, 4: 10, 3: 8, 2: 7, 1: 68, 0: 2}
possibilities = [10, 8, 5, 4, 3, 2, 1, 0]
totalCombinations = 0


def checkIfValid(listToValidate):
    countPointsToValidate = Counter(listToValidate)
    countComb = 1
    for points in countPointsToValidate:
        maxCount = dictPossiblePoints[points]
        thisCount = countPointsToValidate[points]
        # if there are more points in the list to validate
        # then there are numbers with those points, it is not valid
        if thisCount > maxCount:
            countComb = 0
            break
        else:
            # thanks python for actually being able to handle such big numbers as 68!
            countComb *= math.factorial(maxCount)//(
                math.factorial(maxCount-thisCount)*math.factorial(thisCount))
    return countComb


def findPossibleSums(startIndex=0, currentList=None):
    global totalCombinations
    if currentList is None:
        currentList = []
    # go through every element but start only at the index that the previous recursive step ended.
    # this will avoid duplications of the same combination.
    for currentIndex, possibility in enumerate(possibilities[startIndex:], start=startIndex):
        # copy the list
        tempList = currentList[:]

        # append a possibility to the copied list
        tempList.append(possibility)

        # if you have 7 tiles check if it is correct
        if len(tempList) == 7:
            if sum(tempList) == 46:
                countCombinations = checkIfValid(tempList)
                if countCombinations:
                    totalCombinations += countCombinations
                    print(tempList)
                    print("Combinations with these points:", countCombinations)
        # if the list is already over 46 points, there is no point in checking
        elif sum(tempList) <= 46:
            findPossibleSums(currentIndex, tempList)


if __name__ == "__main__":
    print("the possible combinations are:")

    findPossibleSums()
    print("Total combinations: ", totalCombinations)
