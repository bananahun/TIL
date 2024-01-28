authors = [
    '작자 미상',
    '이항복',
    '임제',
    '임제',
    '조성기',
    '조성기',
    '조성기',
    '임제',
    '허균',
    '허균',
    '허균',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '박지원',
    '이항복',
    '남영로',
    '남영로',
    '남영로',
    '이항복',
    '임제',
    '임제',
]
print(set(authors))

new_list = []
for name in authors:
    for new_name in new_list:
        if name != new_name:
            new_list.append(name)
        else:
            pass
        
print (new_list)