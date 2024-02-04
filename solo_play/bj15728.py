N,K = map(int,(input().split()))
share_c = list(map(int, input().split()))
team_c = list(map(int, input().split()))

lst = []
for card_s in share_c:
    for card_t in team_c:
        lst.append(card_s*card_t)
lst.sort()
max_1 = lst[-1]

for card_s in share_c:
    for card_t in team_c:
        if card_s*card_t == max_1:
            team_c.remove(card_t)
            break

new_lst = []
for card_s in share_c:
    for card_t in team_c:
        new_lst.append(card_s*card_t)

new_lst.sort()
max_2 = lst[-1]

for card_s in share_c:
    for card_t in team_c:
        if card_s*card_t == max_2:
            team_c.remove(card_t)
            break

nnew_lst = []
for card_s in share_c:
    for card_t in team_c:
        new_lst.append(card_s*card_t)
nnew_lst.sort()
print(nnew_lst[-1])

# while로 해보자



        




    