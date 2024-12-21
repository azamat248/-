import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Окружность (радиус = {self.radius})"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Квадрат (сторона = {self.side})"


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Треугольник (стороны = {self.a}, {self.b}, {self.c})"


class ShapeFactory:
    def create_shape(self, name):
        if name.lower() == "окружность":
            radius = get_positive_float("Введите радиус круга: ")
            return Circle(radius)
        elif name.lower() == "треугольник":
            a = get_positive_float("Введите сторону a: ")
            b = get_positive_float("Введите сторону b: ")
            c = get_positive_float("Введите сторону c: ")
            return Triangle(a, b, c)
        elif name.lower() == "квадрат":
            side = get_positive_float("Введите сторону квадрата: ")
            return Square(side)
        else:
            raise ValueError("Неизвестный тип фигуры!")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Значение должно быть положительным!")
            else:
                return value
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

factory = ShapeFactory()
figures = []

while True:
    print("\nМеню:")
    print("1. Добавить фигуру")
    print("2. Список фигур")
    print("3. Рассчитать площадь и периметр")
    print("4. Выйти")

    choice = input("Выберите действие: ")
    if choice == "1":
        print("\nВведите тип фигуры:")
        print("Окружность, Квадрат, Треугольник")
        shape_type = input("Введите название фигуры: ")
        try:
            shape = factory.create_shape(shape_type)
            figures.append(shape)
            print(f"{shape} добавлен(а).")
        except ValueError as e:
            print(e)
    elif choice == "2":
        if not figures:
            print("Список фигур пуст.")
        else:
            print("\nСписок фигур:")
            for i, figure in enumerate(figures, start=1):
                print(f"{i}. {figure}")
    elif choice == "3":
        if not figures:
            print("Список фигур пуст.")
        else:
            print("\nВыберите фигуру для расчета:")
            for i, figure in enumerate(figures, start=1):
                print(f"{i}. {figure}")
            try:
                index = int(input("Введите номер фигуры: ")) - 1
                if 0 <= index < len(figures):
                    figure = figures[index]
                    print(f"Площадь: {figure.area():.2f}")
                    print(f"Периметр: {figure.perimeter():.2f}")
                else:
                    print("Некорректный номер.")
            except ValueError:
                print("Некорректный ввод.")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")
