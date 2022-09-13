import random


def new_number(N):   # 몇자리의 게임인지 ? N
    number_gen = set()

    while len(number_gen) < N:
        number_gen.add(random.randint(0, 9))

    return number_gen


def answer(secret_num):
    correct = 0
    count = 1
    exit = 0

    while correct == 0:
        out = 1     # 아웃이 1이면 아웃
        strike, ball = 0, 0
        my_guess = []
        my_guess_num = input('숫자를 맞춰보세요 : ')

        if my_guess_num == 'exit':  # exit 입력하면 끝
            exit = 1
            break

        for i in str(my_guess_num):
            my_guess.append(int(i))

        for i in my_guess:  # 아웃인지 아닌지 판별
            if i in secret_num:
                out = 0
            else:
                continue

        if out == 1:
            print('out!!')
        else:
            for i in range(len(my_guess)):      # 자리까지같은건 스트라이크 숫자만 맞으면 볼
                if my_guess[i] == secret_num[i]:
                    strike += 1
                elif my_guess[i] in secret_num:
                    ball += 1

            if strike == len(secret_num):   # 모두 스트라이크면 끝
                correct = 1
                print('정답입니다!!')
                print(f'시도횟수 : {count}')
                return correct    # 정답시 리턴값 1
            else:
                print(f'{strike}S{ball}B')

        count += 1

    if exit == 1:
        return correct    # exit 입력시 리턴값 0

