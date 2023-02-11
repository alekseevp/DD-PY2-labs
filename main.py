class Car:
    """
    Базовый класс всех машин.

    :param make: str, марка машины
    :param model: str, модель машины
    :param year: int, год выпуска
    :param speed: int, текущая скорость
    """
    def __init__(self, make: str, model: str, year: int, speed: int):
        self.make = make
        self.model = model
        self.year = year
        self._speed = speed

    def __str__(self) -> str:
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self) -> str:
        return f"Car({self.make!r}, {self.model!r}, {self.year!r}, {self._speed!r})"

    def increase_speed(self, speed_increase: int) -> None:
        """
        Увеличивает скорость на опред значение.

        :param speed_increase: int, значение увеличения скорости
        """
        self._speed += speed_increase

    def decrease_speed(self, speed_decrease: int) -> None:
        """
        Уменьшает скорость.

        :param speed_decrease: int, значение уменьшаения скорости
        """
        self._speed -= speed_decrease


class Truck(Car):
    """
    Дочерний класс грузовиков от класса машин.

    :param make: str, марка грузовика
    :param model: str, модель грузовика
    :param year: int, год выпуска
    :param speed: int, теущая скорость
    :param payload_capacity: int, максимальная загрузка
    """
    def __init__(self, make: str, model: str, year: int, speed: int, payload_capacity: int):
        super().__init__(make, model, year, speed)
        self.payload_capacity = payload_capacity

    def __str__(self) -> str:
        return f"{super().__str__()} с максимальной загрузкой {self.payload_capacity} кг"

    def __repr__(self) -> str:
        return f"Truck({super().__repr__()}, {self.payload_capacity!r})"

    def decrease_speed(self, speed_decrease: int) -> None:
        """
        Уменьшает скорость грузовика.
        Для грузовиков при снижении скорости необходимо учитывать их вес и грузоподъемность.

        :param speed_decrease: int, значения уменьшения скорости
        """
        self._speed -= speed_decrease * (1 + self.payload_capacity / 1000)
