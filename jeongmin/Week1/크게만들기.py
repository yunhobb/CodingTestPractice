"""

    N자리 숫자가 주어졌을 때
    숫자 K개를 지워서 얻을 수 있는 가장 큰 수

"""

if __name__ == '__main__':
    N, K = map(int, input().split())
    number = list(input())

    find = []
    i = 0 # 버린 카드의 수
    for num in number:
        while i < K and find and find[-1] < num:
            find.pop()
            i += 1
        if len(find) < (N-K):
            find.append(num)

    print(''.join(find))

