import sys

input = sys.stdin.readline()

L, R = map(int, input.split())

def check8(L, R):
    # print(len(str(L)))
    # print(len(str(R)))
    result = 0
    cnt_L = 0
    cnt_R = 0
    if len(str(L)) != len(str(R)):
        return result
    elif '8' not in str(L):
        return result
    elif '8' not in str(R):
        return result
    else:
        for i in range(len(str(L))):
            # print(str(R)[i])
            # print(str(L)[i])
            if str(L)[i] == str(R)[i]:
                if str(L)[i] == '8':
                    result += 1
            else:
                return result
        return result
print(check8(L, R))