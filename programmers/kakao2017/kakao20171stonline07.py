import re
import copy
def solution(lines):
    p = re.compile("2016-09-15 ([0-9])+:([0-9])+:(.+) (.+?)s")
    lines = [re.findall(p, line) for line in lines]
    logs = list()
    lines = [ list(line[0]) for line in lines]
    for log in lines:
        log[0], log[1], log[2], log[3] = int(log[0]), int(log[1]), float(log[2]), float(log[3])
        temp = [int((log[0]*360 + log[1]*60 + log[2]-log[3])*1000)+1, int((log[0]*360 + log[1]*60 + log[2])*1000)]
        logs.append(temp)
    maxthrouhput = 0
    for idx in range(len(logs)):
        temp = 0
        for jdx in range(len(logs)):
            if idx == jdx:
                continue
            else:
                if 0 < logs[idx][0] - logs[jdx][1] < 1000:
                    temp += 1
        if maxthrouhput < temp:
            maxthrouhput = temp

    print(logs)
    print(maxthrouhput)
    return 0


solution([ "2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s" ])