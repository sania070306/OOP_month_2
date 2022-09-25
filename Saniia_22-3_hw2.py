class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self)
        self.__radius = radius

    def calculate_area(self):
        a = 3.14 * (self.__radius**2)
        return a

    def info(self):
        print(f'Circle radius: {self.__radius}{Figure.unit}, Area:{self.calculate_area()}{Figure.unit}')

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        Figure.__init__(self)
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f'RightTriangle side a: {self.__side_a}{Figure.unit} , side b: {self.__side_b}{Figure.unit}, Area: {self.calculate_area()}{Figure.unit}.')

circle1 = Circle(5)
circle2 = Circle(2)
rightTriangle1 = RightTriangle(5, 3)
rightTriangle2 = RightTriangle(6,8)
rightTriangle3 = RightTriangle(4,7)
figure = [circle1, circle2, rightTriangle1, rightTriangle2, rightTriangle3]

for i in figure:
    print(i.info())