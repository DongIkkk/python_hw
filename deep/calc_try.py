class Calc:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print('0으로는 나눌 수 없습니다.')
            return '계산할 수 없음'


calc = Calc()

print('계산하려는 두 숫자를 입력해주세요 :', end=" ")

try:
    a, b = map(int, input().split())
    calc.set_number(a, b)
    print(f'더한 값 : {calc.plus()}')
    print(f'뺀 값 : {calc.minus()}')
    print(f'곱한 값 : {calc.multiple()}')
    print(f'나눈 값 : {calc.divide()}')
except ValueError:
    print('숫자만 입력할 수 있습니다.')
