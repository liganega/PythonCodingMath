a = [1,2,3]
b = [3,4,5]

c = []                     # 합집합을 우선 공집합으로 만들어 놓고
for i in a:                # a의 원소 i에 대해
    if i not in c:         # c에 없으면
        c.append(i)        # c에 그 원소 i를 넣어라

for i in b:                # b의 원소 i에 대해
    if i not in c:         # c에 없으면
        c.append(i)        # c에 그 원소 i를 넣어라
c.sort()
print(c)
