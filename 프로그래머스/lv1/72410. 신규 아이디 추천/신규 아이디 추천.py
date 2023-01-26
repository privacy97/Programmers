def solution(new_id):
    
    #1단계
    new_id = new_id.lower()
        
    #2단계
    temp = ''
    new_id = list(new_id)
    for i in new_id:
        if ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9') or i in ['-', '_', '.']:
            temp += i
    new_id = temp
    
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    #4단계
    new_id = list(new_id)
    if new_id[0] == '.':
        new_id[0] = ''
    if new_id[-1] == '.':
        new_id[-1] = ''
    new_id = ''.join(new_id)
    
    #5단계
    if new_id == '':
        new_id = 'a'
        
    #6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    #7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    answer = new_id
    return answer