def solution(spell, dic):
    answer = 2
    for i in dic:
        count = 0
        for j in spell:
            if j in list(i):
                count += 1
            i = i.replace(j, '', 1)
        if i == '' and count == len(spell):
            answer = 1
            break
    return answer