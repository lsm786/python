import random

a = random.randrange(1, 10)
count = 0
max_try = 5

print('숫자 맞추기 게임을 시작합니다.')
print('1에서 10까지 숫자중 하나의 숫자가 랜덤으로 나오며, 그 숫자를 맞추면 당신이 이기게 됩니다.')
print('당신이 말한 숫자와 랜덤 숫자가 다르면 업, 다운으로 힌트를 드립니다.')
print('그럼 건투를 빕니다.')

while count < max_try:
    b = int(input('숫자를 입력하세요: '))
    count += 1

    if b == a:
        print('정답!! 🎉')
        break
    elif b > a:
        print('다운')
    else:
        print('업')

    print(f'남은 기회: {max_try - count}번')

if count == max_try and b != a:
    print(f'실패! 정답은 {a}였습니다.')

