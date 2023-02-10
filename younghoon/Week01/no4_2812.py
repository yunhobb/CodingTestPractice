import sys

# 입력
N, K = map(int, input().split())

# 입력 N자리수
num = list(str(input()))


def large_num(num):
    # 정답
    answer = ''
    # 삭제한 수
    skip = 0
    # K번째 자리수까지는 작은 수 제거
    prev_max = max(num[:K])
    prev_max_idx = num.index(prev_max)
    # K+1번째 수
    check = num[K+1]
    # 앞에 K개의 숫자가 K+1보다 작으면 앞에 K개를 제거하는 것이 가장 큼
    all_pass = False
    if prev_max < check:
        answer = "".join(num[K:])
        all_pass = True

    # K번째까지 수에서 최대로 하는 값 확인
    if not all_pass:
        skip += 1
        answer = num[prev_max_idx]
        for idx in range(prev_max_idx+1, K):
            if num[idx] < prev_max:
                skip += 1
            else:
                answer += num[idx]

    post_max = max(num[K:])
    post_max_index = num.index(post_max)
    if N - post_max_index + len(answer) >= N- K:
        for idx in range(post_max_index+1, N):
            if skip == K:
                i = idx-1
                while len(answer) < N - K:
                    answer += num[i]
                    i += 1
            if num[idx] < post_max:
                skip += 1
            else:
                ansewr += num[idx]
            
    # 나머지 자리에서 가장 큰 수를 뽑도록 자릿수를 비교
    for idx in range(K, N-1):
        if all_pass:
            break
        # K개를 모두 뽑은 경우 남은 숫자들이 정답 + 이후 확인 불필요
        if skip == K:
            i = idx-1
            while len(answer) < N - K:
            # answer += "".join(num[idx-1:idx-1+N-2*K])
            # break
                answer += num[i]
                i += 1
        if len(answer) == N-K:
            break
    
        # 이전 숫자가 다음 숫자보다 작은 경우 패스
        if num[idx] < num[idx+1]:
            skip += 1
        # 이전 숫자가 다음 숫자보다 큰 경우 해당 경우가 정답
        else:
            answer += num[idx]
    
    # 예외처리
    if len(answer) == N-K-1:
        answer += num[-1]

    return answer


# prev = num[:K]
# post = num[K:]
# prev_max = max(prev)
# post_max = max(post)
# get = 0

# if prev_max < post[0]:
#     answer = ''.join(post)
#     print(answer)

# elif prev_max == post[0]:
#     get = 2
#     for pos in post:
#         if get == N-K:
#             break
        
# else:
#     for pre in prev:
#         if pre == prev_max:
#             answer += pre
#             get += 1
#     for pos in post:
#         if get == N-K:
#             break
        
print(large_num(num))