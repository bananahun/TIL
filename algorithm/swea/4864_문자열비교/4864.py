import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def brute_force(pattern, target):
    pattern_index = 0
    target_index = 0
    while target_index < len(target):
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        target_index += 1
        pattern_index += 1

        if pattern_index == len(pattern):
            return True
    return False


def KMP(pattern, target):
    def make_lps():
        lps = [0] * (len(pattern) + 1)
        for idx in range(1, len(pattern)):
            if pattern[lps[idx - 1]] == pattern[idx]:
                lps[idx + 1] == lps[idx] + 1
        lps.insert(0, -1)
        return lps

    lps = make_lps()

    pattern_index = 0
    target_index = 0
    # print(lps)
    while target_index < len(target):

        # print(lps[pattern_index])
        # print(target_index, target[target_index], pattern_index, pattern[pattern_index])
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        target_index += 1
        pattern_index += 1

        if pattern_index == len(pattern):
            return True
    return False
    print(lps)


def boyer_moore(pattern,target):
    lps = {pattern[idx]: len(pattern) -1 - idx for idx in range(len(pattern))}
    pattern_index = len(pattern)
    target_index = 0

    while target_index <= len(target) - pattern_index:
        for p_idx in range(pattern_index-1,-1,-1):
            if target[target_index + p_idx] != pattern[p_idx]:
                target_index += lps.get(target[target_index + p_idx]), len(pattern)
                break
        else:
            return True


for tc in range(1, T + 1):
    str_1 = input()
    str_2 = input()
    if str_1 in str_2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    # boyer_moore(str_1,str_2)

