def solution(sides):
    sides.sort()
    if sides[-1] >= (sides[0] + sides[1]):
        answer = 2
    else:
        answer = 1
    return answer