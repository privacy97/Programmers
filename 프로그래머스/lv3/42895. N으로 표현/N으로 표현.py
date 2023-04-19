'''
1. DP문제인지 확인
   - 식을 세워서 문제를 해결할 수 있는가?
   - 작은 문제로 큰 문제 해결할 수 있는가?
   
2. DP 점화식 세우기 (작은 문제 파악)

N을 최소로 사용해서 number를 만드는 것이 목표

N을 1개 사용해서 표현할 수 있는 수의 집합은?
N을 2개 사용해서 표현할 수 있는 수의 집합은?
N을 3개 사용해서 표현할 수 있는 수의 집합은?
                  .
                  .
                  .


N = 5 일 때

N을 1개 사용 (1개)
5

N을 2개 사용 (5개)
55,
(5+5), (5-5), (5/5), (5*5)

N을 3개 사용 (41개)
555,

55+5, 55-5, 55/5, 55*5,
5+55, 5-55, 5/55, 5*55,

(5+5)+5, (5+5)-5, (5+5)/5, (5+5)*5,
(5-5)+5, (5-5)-5, (5-5)/5, (5-5)*5,
(5/5)+5, (5/5)-5, (5/5)/5, (5/5)*5,
(5*5)+5, (5*5)-5, (5*5)/5, (5*5)*5,

5+(5+5), 5-(5+5), 5/(5+5), 5*(5+5),
5+(5-5), 5-(5-5), 5/(5-5), 5*(5-5),
5+(5/5), 5-(5/5), 5/(5/5), 5*(5/5),
5+(5*5), 5-(5*5), 5/(5*5), 5*(5*5)

                  .
                  .
                  .
'''

def solution(N, number):
    
    # 에외처리 : 1일 땐 1이죠
    if number == 1:
        return 1
    
    
    # N 사용개수 별 계산결과를 담을 리스트
    set_list = []
    
    
    # 조건1. N은 1이상 9이하입니다.
    for cnt in range(1, 4):
        
        
        # N 사용개수 별 계산결과 집합 만들기(중복 수 제외를 위한 집합)
        partial_set = set()
        
        
        # N 사용개수에 따라서 집합에 이어붙인 숫자 넣기
        print('N 사용 횟수 :', cnt)
        print()
        print((str(N) * cnt)+',')
        partial_set.add(int(str(N) * cnt))
        
        
        # 이전에 생성된 모든 숫자에 앞,뒤로 사칙연산 후 집합에 추가
        for i in range(len(set_list)):
            for op1 in set_list[i]:
                for op2 in set_list[-i-1]:
                    
                    print(str(op1)+'+'+str(op2), end=', ')
                    partial_set.add(op1 + op2)
                    
                    print(str(op1)+'-'+str(op2), end=', ')
                    partial_set.add(op1 - op2)
                    
                    print(str(op1)+'*'+str(op2), end=', ')
                    partial_set.add(op1 * op2)
                    
                    # 예외처리 : 0 나누기는 안돼요~~
                    print(str(op1)+'/'+str(op2))
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        
        # 집합에서 number 확인, 존재 시 N 사용개수 return
        if number in partial_set:
            return cnt
        
        # N 사용개수
        set_list.append(partial_set)
        print(set_list)
        print()
        print()
    
    
    # 전체 실행 후에도 답이 안 나온다면, return -1
    return -1


def solution(N, number):
    
    if number == 1:
        return 1

    set_list = []
    
    for cnt in range(1, 9):
        
        partial_set = set()
        partial_set.add(int(str(N) * cnt))
        
        for i in range(len(set_list)):
            for op1 in set_list[i]:
                for op2 in set_list[-i-1]:
                    
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 - op2)
                    partial_set.add(op1 * op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        
        if number in partial_set:
            return cnt

        set_list.append(partial_set)
    
    return -1