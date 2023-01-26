import copy

def solution(emergency):
    #return sorted(range(len(emergency)), key=lambda k: emergency[k], reverse=True)
    copy_e = copy.deepcopy(emergency)
    copy_e = sorted(copy_e, reverse=True)
    print(emergency, copy_e)
    for i in range(1, len(emergency)+1):
        emergency[i-1] = copy_e.index(emergency[i-1])+1
        
    return emergency