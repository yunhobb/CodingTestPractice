import sys
def five_two(money):
    # 거스름돈 불가능
    if money == 1 or money == 3:
        return -1

    else:
        # 동전개수
        cnt = 0
        while money % 5 != 0:
            money -= 2
            cnt += 1
        cnt += money // 5

        return cnt
# 거스름돈
money = int(input())

print(five_two(money))