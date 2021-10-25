from sys import stdin

while True:
    str_input = stdin.readline().rstrip()  # 오른쪽 공백 삭제

    a = ''

    if str_input == '.':
        break

    for s in str_input:
        if s == '(':
            a += '('
        elif s == ')':
            a += ')'
        elif s == '[':
            a += '['
        elif s == ']':
            a += ']'

    for _ in range(len(a) // 2):
        a = a.replace('()', '')
        a = a.replace('[]', '')

    if a == '':
        print('yes')
    else:
        print('no')
