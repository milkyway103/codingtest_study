# 09:00부터 총 n회 t분 간격으로 역에 도착
# 하나의 셔틀에는 최대 m명의 승객이 탑승 가능
# 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루까지 탑승 가능
# 구할 것 : 셔틀을 타고 사무실로 갈 수 있는 도착 시간 중 제일 늦은 시각
import operator
def solution(n, t, m, timetable):
    result = ""
    newtimetable = list()
    for time in timetable:
        # time을 하나의 수로 변환
        print(time)
        newtimetable.append(int(time[0:2])*60 + int(time[3:5]))
    shuttle = Shuttle(n, t, m)
    for crew in newtimetable:
        shuttle.goonshuttle(crew)
    shuttledict = shuttle.getshuttle()

    ison = 0
    target = shuttle.timelist[-1]
    if len(shuttledict[target]) < m:
        ison = target
    else:
        ison = shuttledict[target][-1]-1
    hh, mm = divmod(ison, 60)
    if hh < 10:
        result = result + "0" + str(hh) + ":"
    else:
        result = str(hh) + ":"
    if mm < 10:
        result = result + "0" + str(mm)
    else:
        result = result + str(mm)
    print(result)
    return result

class Shuttle:
    def __init__(self, n, t, m):
        self.timelist = [540]
        for idx in range(1,n):
            self.timelist.append(540+(idx*t))
        self.m = m
        self.shuttledict = { time:list() for time in self.timelist}
    def goonshuttle(self, crew):
        for key in self.shuttledict.keys():
            if key < crew:
                continue
            else:
                if len(self.shuttledict[key]) < self.m:
                    self.shuttledict[key].append(crew)
                    break
    def getshuttle(self):
        for key in self.shuttledict.keys():
            self.shuttledict[key] = sorted(self.shuttledict[key])
        return self.shuttledict

solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
