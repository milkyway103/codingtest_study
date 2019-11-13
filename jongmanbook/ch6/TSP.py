'''
shortestPath(path) = path가 지금까지 만든 경로일 때,
나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환한다.
'''

def shortestpath(n, dist, path, visited, currentLength):
    '''
    :param n: 도시의 수
    :param dist: 두 도시 간의 거리를 저장하는 배열
    :param path: 지금까지 만든 경로
    :param visited: 각 도시의 방문 여부
    :param currentLength: 지금까지 만든 경로의 길이
    :return: 나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환
    '''
    # 기저 사례 : 모든 도시를 다 방문했을 때는 시작 도시로 돌아가고 종료
    if len(path) == n:
        return currentLength + dist[path[0]][path[-1]]
    ret = float('inf') # 매우 큰 값으로 초기화
    # 다음 방문할 도시를 전부 시도해 본다.
    for next in range(n):
        if visited[next]:
            continue
        here = path[-1]
        path.append(next)
        visited[next] = True
        # 나머지 경로를 재귀 호출을 통해 완성하고 가장 짧은 경로의 길이를 얻는다.
        cand = shortestpath(n, dist, path, visited, currentLength + dist[path[here]][path[next]])
        ret = min(ret, cand);
        visited[next] = False
        path.pop(-1)
    return ret


def solve(n, dist):
    answer = list()
    return list()