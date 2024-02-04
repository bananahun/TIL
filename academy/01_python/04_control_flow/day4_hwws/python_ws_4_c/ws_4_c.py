matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0

for m in range(len(matrix)):
    matrix_len = matrix_len+1
print(matrix_len)

for m in range(len(matrix)):
    for n in range(len(matrix[m])):
        pass           
    print(f'{matrix[m]}리스트는 {n+1}개 만큼 요소를 가지고 있습니다.')

for m in range(len(matrix)):
    for n in range(len(matrix[m])):
        print(f'matrix의{m},{n}번째 요소의 값은{matrix[m][n]}입니다.')

