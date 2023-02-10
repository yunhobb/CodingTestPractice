import sys

# 입력
N = int(input())

# 최소비용을 구하기 위해 비용을 내림차순으로 정렬
cost = sorted(list(int(input()) for _ in range(N)), reverse=True)

# 최소비용
money = 0

# 세 묶음씩 사면서 최솟값을 버림 (내림차순 정렬)
for c in range(len(cost)//3):
    money += sum(cost[3*c : 3*c + 2])
money += sum(cost[(len(cost)//3)*3:])

print(money)