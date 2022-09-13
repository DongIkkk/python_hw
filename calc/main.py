from calc_function import *

print('계산 하려는 숫자 두개를 입력하세요 :', end=' ')
a, b = map(int, input().split())
print('연산기호를 입력하세요(+, -, *, /) :', end=' ')
what = input()

if what == '+':
    print(cal_sum(a, b))
elif what == '-':
    print(cal_sub(a, b))
elif what == '*':
    print(cal_mul(a, b))
elif what == '/':
    result = cal_div(a, b)
    print(f'{result:.3f}')
else:
    print('잘못 입력 하셨습니다!')
