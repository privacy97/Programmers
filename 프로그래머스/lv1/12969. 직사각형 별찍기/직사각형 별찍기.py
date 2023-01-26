a, b = map(int, input().strip().split(' '))

for i in range(b):
    s = ''
    for j in range(a):
        s += '*'
    print(s)
    