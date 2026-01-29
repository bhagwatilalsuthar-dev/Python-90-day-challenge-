# 1
Sum=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def finder(findOfRowSum):
    finderList=[]
    for findSum in findOfRowSum:
        finderList.append(max(findSum))
    print(finderList)
finder(Sum)
# 2
matrix = [
    [3, 1, 7],
    [2, 8, 4],
    [9, 10, 6]
]
def maxValueFinder(eachColumnMax):
    myList = []
# Column wise maximum
    for x in range(len(eachColumnMax[0])):   # Step 1: Column loop
        maxVal = eachColumnMax[0][x]         # Step 2: Initialize max for this column
        for y in range(len(eachColumnMax)):  # Step 3: Row loop
            if eachColumnMax[y][x] > maxVal:  # Step 4: Compare & update
                maxVal = eachColumnMax[y][x]
        myList.append(maxVal)         # Step 5: Add column max to list
    print(myList)
# maxValueFinder(matrix)
# 3
matrix=[[1, 2, 3],
        [4, 5, 6]]
def matrixTransposer(matTransList):
    myTransposerList=[]
    rows=len(matTransList)
    cols=len(matTransList[0])
    for eachItem in range(cols):
        myList=[]
        for transposer in range(rows):
            myList.append(0)
        myTransposerList.append(myList)
    # print(myTransposerList)
    for eachItem in range(rows):
        for transposer in range(cols):
            myTransposerList[transposer][eachItem]=matTransList[eachItem][transposer]
    print(myTransposerList)

# matrixTransposer(matrix)
# 4
digonalSum=[[1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]]
def digonalSumFinder(sumOfList):
    index=0
    i=0
    myList=[]
    while index<len(sumOfList):
        myList.append(sumOfList[index][i])
        # print(eachColumnMax[index][i])
        index+=1
        i+=1
    
    print(sum(myList))
# digonalSumFinder(digonalSum)
matrix = [
    [3, 1, 7],
    [2, 8, 4],
    [9, 10, 6]
]
for x in matrix:
    print(min(x))