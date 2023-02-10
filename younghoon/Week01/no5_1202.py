import sys
import time
# N: 보석 개수, K: 가방 개수 입력
N, K = map(int, input().split())

# 보석 정보 jew[0][idx]: 보석 무게 jew[1][idx]: 보석 가격 (보석 무게 기준 내림차순 정렬)
jews = sorted(list(list(map(int, sys.stdin.readline().split())) for _ in range(N)), key=lambda x: x[1], reverse=True)

# 가방 정보 bag[idx]: 각 가방에 들어가는 최대 무게 (오름차순 정렬)
bags = sorted(list(int(input()) for _ in range(K)))
# mt = time.time()

# print(f'{mt-st:5f} sec')
# print(f'보석 정보: {jews}\n가방 정보: {bags}')
st = time.time()
# 훔친 보석 가격
steel = []

# 보석정보 및 가방 정보 index
while len(steel) < K:
    idx = -1
    for jew in jews:
        for idx in range(len(bags)):
            # print(f'훔친보석: {steel} // 남은 가방: {bags}')
            if jew[0] < bags[idx]:
                steel.append(jew[1])
                del bags[idx]
                break
# print(f'훔친보석: {steel} // 남은 가방: {bags}')
print(sum(steel))
et = time.time()
print(f'{et-st: 5f} sec')