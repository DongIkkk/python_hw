number_count = 0

while number_count < 5:
    user = input()
    if user.isdigit():
        print(int(user) * 2)
        number_count += 1
    elif user.isalpha:
        if user == 'exit':
            break
        print(f'입력한 문자는 {user}입니다.')
