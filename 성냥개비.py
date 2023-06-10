import random
b = random.randint(7,100)
print(b)

if b % 4 == 1:
    b += 2


matchsticks = b

print("1.성냥개비 게임을 시작한다.")
print("2.게임 규칙: 각 플레이어는 1개 이상, 3개 이하의 성냥개비를 가져갈 수 있다.")
print("3.마지막 성냥개비를 가져가는 플레이어가 패배한다.")
print("\n현재 성냥개비 개수:",matchsticks)

if b % 4 == 2:
    matchsticks -= 1

elif b % 4 == 3:
    matchsticks -= 2

elif b % 4 == 4:
    matchsticks -= 3

while True:
    print()
    print('ai가 성냥개비를 가져갔습니다.')
    print("\n현재 성냥개비 개수:",matchsticks)

    while True:
        player_choice = int(input("성냥개비 말이다. 몇개고? (1~3): "))

        if player_choice >= 4 or player_choice == 0:
            print("장난치지마!")
            break

        elif 1 <= player_choice <= 3:
            print('잘했어요! 행운을 빕니다!!')
            print()

        matchsticks -= player_choice

        if matchsticks <= 0:
            print("\n마지막 성냥개비를 가져간 플레이어가 패배했습니다. '닝겐!!! 너의 심장을 가져가겠다!!!'")
            break
        a = ['후후...애송이 그정도밖에 되지않는가!' , '좀 치는군?!' , '잘하는데?','제법이군...닝겐..']
        i = random.randint(0,3)
        print(a[i])

        ai = 0

        if player_choice == 3:
            matchsticks -= 1
            print()
            print('[ai가 성냥개비를 1개 가져갔습니다].')

        elif player_choice == 2:
            matchsticks -= 2
            print()
            print('[ai가 성냥개비를 2개 가져갔습니다].')

        else:
            matchsticks -= 3
            print()
            print('[ai가 성냥개비를 3개 가져갔습니다].')

        print("남은 성냥개비 개수:", matchsticks)

        if matchsticks <= 0:
            print("\n마지막 성냥개비를 가져간 플레이어가 패배했습니다. 얼른 뛰어내리세요!!")
            break
    if matchsticks <= 0:
        break
