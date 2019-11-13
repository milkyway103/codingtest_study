def solution(cacheSize, cities):
    cities = [_.lower() for _ in cities]
    runtime = 0
    if cacheSize == 0:
        runtime = 5*len(cities)
        print(runtime)
        return runtime
    cache = LRUCache(cacheSize)
    for idx, city in enumerate(cities):
        runtime+=cache.putitem(city, idx)

    print(runtime)
    return runtime

class LRUCache:
    def __init__(self, cachesize):
        self.map = dict()
        self.size = cachesize
    def putitem(self, item, id):
        if item in self.map.keys():
            self.map[item] = id
            return 1
        else:
            if len(self.map) < self.size:
                self.map[item] = id
            else:
                victim = None
                for key in self.map.keys():
                    if victim == None:
                        victim = key
                        continue
                    if self.map[key] < self.map[victim]:
                        victim = key
                del(self.map[victim])
                self.map[item] = id
            return 5





solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
