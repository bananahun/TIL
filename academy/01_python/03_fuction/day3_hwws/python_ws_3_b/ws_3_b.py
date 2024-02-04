pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject,day,title=None):
    data = {'과목':subject,'일차':day,'제목':title,'문제번호':pro_num}
    
    return data
pro_num += 1
result_1 = create_data('python',3)
pro_num += 1
result_2 = create_data('web',1,'web연습하기')
pro_num += 1
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)
