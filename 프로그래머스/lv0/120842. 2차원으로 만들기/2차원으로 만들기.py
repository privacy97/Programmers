def solution(num_list, n):
    return [ num_list[x-n:x] for x in range(n, len(num_list)+1, n) ]