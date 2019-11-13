cand = []
ban_dict = dict()


def solution(user_id, banned_id):
    answer = 0
    global cand, ban_dict

    for ban in banned_id:
        if ban in ban_dict.keys():
            continue
        ban_dict[ban] = []
        for user in user_id:
            if len(user) == len(ban):
                ismatched = True
                for idx in range(len(ban)):
                    if ban[idx] == '*':
                        continue
                    if ban[idx] != user[idx]:
                        ismatched = False
                if ismatched:
                    ban_dict[ban].append(user)

    match([], banned_id, user_id, 0)
    print(cand)
    answer = len(cand)

    return answer


def match(check, banned_id, user_id, next_ban):
    global cand, ban_dict
    if next_ban == len(banned_id):
        check.sort()
        if check not in cand:
            cand.append(check[:])
        return
    cur = banned_id[next_ban]
    for user in ban_dict[cur]:
        if user not in check:
            check.append(user)
            match(check, banned_id, user_id, next_ban + 1)
            check.pop(-1)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))