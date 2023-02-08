"""

    백준: https://www.acmicpc.net/problem/14916
    2원과 5원짜리로만 거스름돈을 달라고 함.

    15 => 5원 3개

"""
MAX = 100001

def solution(c):
    dp = [MAX] * (c + 1)
    money = [2, 5]
    min_base = min(money)
    for i in range(min_base, c+1):

        if i in money:
            dp[i] = 1
        for base in money:
            if i > base:
                dp[i] = min(dp[i], dp[i-base] + 1)

    if dp[c] == MAX:
        return -1
    return dp[c]


if __name__ == '__main__':
    change = int(input())

    print(solution(change))
