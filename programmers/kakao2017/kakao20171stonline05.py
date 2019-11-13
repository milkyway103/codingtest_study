import re
from collections import defaultdict
def solution(str1, str2):
    str1list = list()
    str2list = list()
    str1dict = defaultdict(int)
    str2dict = defaultdict(int)
    notengfilter = re.compile("[^A-Za-z]")

    for idx in range(len(str1)-1):
        str1list.append(str1[idx:idx+2])
    for idx in range(len(str2)-1):
        str2list.append(str2[idx:idx+2])

    str1list = [val.lower() for val in str1list if re.search(notengfilter, val) == None]
    str2list = [val.lower() for val in str2list if re.search(notengfilter, val) == None]

    if str1list == [] or str2list == []:
        return 65536

    for item in str1list:
        str1dict[item] += 1
    for item in str2list:
        str2dict[item] += 1

    gyo = 0
    hap = 0
    for key in str1dict.keys():
        if key in str2dict.keys():
            gyo += min(str1dict[key], str2dict[key])
            hap += max(str1dict[key], str2dict[key])
        else:
            hap += str1dict[key]
    for key in str2dict.keys():
        if key not in str1dict.keys():
            hap += str2dict[key]

    result = int(gyo/hap * 65536)

    return result

def jacard(intersection, outersection):
    return len(intersection)/len(outersection)

print(solution("E=M*C^2", "e=m*c^2"))