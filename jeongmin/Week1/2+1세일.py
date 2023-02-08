"""

    백준: https://www.acmicpc.net/problem/11508

    유제품을 3개를 한 번에 산다면 그 중에서 가장 싼것은 무료로 지불
    나머지 두개의 제품 가격만 지불하면 된다.

    첫번째 줄에는 유제품의 수 N

    각 유제품의 가격 Ci가 주어짐

    10 9 4 2 6 4 3
    10 9 6 4 4 3 2

    가격을 높은 순으로 정렬하고

    전체 금액에서 최대한 높은 가격을 가진 물품이 할인행사할 수 있도록 정해줌.

"""

def solution(p):
    p.sort(reverse=True)
    pay = sum(p)
    sales = 0

    for i in range(2, len(p), 3):
        sales += p[i]

    pay -= sales
    return pay


if __name__ == '__main__':
    N = int(input())
    prices = [int(input()) for _ in range(N)]

    print(solution(prices))
