class Area:
    PIE = 3.14  # 원의 넓이 계산 파이값

    def __init__(self, width, length):  # 인스턴스 생성시 가로 세로 길이 받는다
        self.width = width
        self.length = length
        self.radius = self.width / 2

    def square(self):       # 사각형의 넓이
        return self.width * self.length

    def triangle(self):     # 삼각형의 넓이
        return self.width * self.length / 2

    def circle(self):       # 원의 넓이
        return self.radius * self.radius * Area.PIE


area = Area(10, 20)

print(area.square())
print(area.triangle())
print(area.circle())
