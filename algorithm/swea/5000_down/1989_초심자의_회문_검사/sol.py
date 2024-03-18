import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()

    if string == str(''.join(reversed(string))):
        print(f'{tc} 1')
    else:
        print(f'{tc} 0')