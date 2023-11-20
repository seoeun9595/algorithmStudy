def solution(array):
    setA = set(array)
    cntDict = {}
    for i in setA:
        cntDict[i] = array.count(i)

    vList = list(cntDict.values())
    maxValue = max(vList)
    vList.remove(maxValue)

    if maxValue in vList:
        return -1
    else:
        for key, value in cntDict.items():
            if value == maxValue:
                return key
