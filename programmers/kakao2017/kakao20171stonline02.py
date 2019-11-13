import re
def solution(dartResult):
    result = 0
    splitdart = re.compile("([0-9]+[^0-9]+)")
    searchint = re.compile("([0-9]+)")
    dartlist = splitdart.findall(dartResult)
    dartintlist = searchint.findall(dartResult)
    dartintlist = list(map(int, dartintlist))
    resultlist = list()
    for idx in range(3):
        temp = dartintlist[idx]
        for jdx in range(len(dartlist[idx])):
            if dartlist[idx][jdx] == "D":
                temp = temp**2
            if dartlist[idx][jdx] == "T":
                temp = temp**3
            if dartlist[idx][jdx] == "*":
                temp *= 2
                if idx > 0:
                    resultlist[idx-1] *= 2
            if dartlist[idx][jdx] == "#":
                temp = -temp
        resultlist.append(temp)
    return sum(resultlist)

dartResult = "1S2D*3T"
print(solution("1D2S3T*"))