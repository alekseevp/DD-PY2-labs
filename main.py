class Car:
    """Базовый класс машины.

    Атрибуты:
        make (str): Марка машины.
        model (str): Модель машины.
        year (int): Год выпуска.
        speed (int): Скорость машины.

    """

    def __init__(self, make: str, model: str, year: int, speed: int):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

    def __repr__(self):
        return f'Car({self.make!r}, {self.model!r}, {self.year!r}, {self.speed!r})'

    def accelerate(self):
        """Увеличить скорость на 10."""
        self.speed += 10

    def brake(self):
        """Уменьшить скорость на 10."""
        self.speed -= 10


class Truck(Car):
    """Дочерний класс грузовика.

    Атрибуты:
        make (str): Марка грузовика.
        model (str): Модель грузовика.
        year (int): Год выпуска грузовика.
        speed (int): Скорость грузовика.
        load_capacity (int): Максимальная загрузка грузовика.

    """

    def __init__(self, make: str, model: str, year: int, speed: int, load_capacity: int):
        super().__init__(make, model, year, speed)
        self.load_capacity = load_capacity

    def __str__(self):
        return f'{self.make} {self.model} ({self.year}) загруженный на {self.load_capacity} кг'

    def brake(self):
        """Уменшает скорость грузовика на 10.

        Этот метод пегеружает brake метод базового класса. Это необходимо поскольку грузовики как правило тяжелее
        обычных машин и требуют более сильных тормозов.
        """
        self.speed -= 20