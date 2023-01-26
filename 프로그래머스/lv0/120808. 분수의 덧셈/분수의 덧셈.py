
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    down = num1 * num2
    up = denum1 * num2 + denum2 * num1
    gcd_num = gcd(down, up)
    answer = [up / gcd_num, down / gcd_num]
    return answer