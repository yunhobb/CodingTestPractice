import sys

# 입력 (회의 수)
N = int(input())

# 시작, 종료시간 입력
s_time_e = []
for info in range(N):
    s, e = map(int, sys.stdin.readline().split())
    s_time_e.append([s, e])

# 시작시간기준 오름차순 정렬
s_time_e.sort()

# 회의들 첫번째를 default로 넣음
meeting = [[s_time_e[0][0], s_time_e[0][1]]]

# 시작시간을 기준으로 회의가 끝나는 시간과 시작하는 시간을 비교하여 meeting 배열에 append
for idx in range(1, N):
    # 앞선 회의가 더 빨리 끝나는 경우
    if meeting[-1][1] <= s_time_e[idx][1]:
        # 바로 뒤 회의 시작 시간과 회의 종료시간을 비교
        if meeting[-1][1] <= s_time_e[idx][0]:
            meeting.append(s_time_e[idx])
    
    # 뒤 회의가 더 일찍 끝나는 경우
    else:
        meeting.pop()
        meeting.append(s_time_e[idx])
        
print(len(meeting))