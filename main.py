import doctest


class Character:
    def __init__(self, name: str, hp: float, mana: float):
        """
        Персонаж настолки
        :param name: Имя персонажа
        :param hp:  здоровье персонажа, текущее
        :param mana:  мана персонажа, теущая
        Примеры:
        >>> character = Character("John", 100, 100)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя персонажа должно быть типа str")
        self.name = name
        self.max_hp = 100  # Максимальное здоровье персонажа
        self.armor = 10  # Защита брони
        if not isinstance(hp, int):
            raise TypeError("Здоровье персонажа должен быть типа int")
        if hp <= 0:
            raise ValueError("Персонаж умер")
        if hp > self.max_hp:
            raise ValueError("Выше максимального здоровья(100)")
        self.hp = hp
        self.max_mana = 100  # Максимальное мана персонажа
        if not isinstance(mana, int):
            raise TypeError("Мана персонажа должно быть типа int")
        if mana <= 0:
            raise ValueError("Мана персонажа не может быть отрицательной")
        if mana > self.max_mana:
            raise ValueError("Выше максимальной маны (100)")
        self.mana = mana

    def hit(self, damage: int):
        """"
        Пусть персонажа пытаются атаковать. Тогда урон будет определяться как урон оружия минус броня.
        :param damage: Урон оружия
        :raise ValueError: Если после атаки здоровье персонажа меньше нуля, он умирает
        :return: Здоровье персонажа после получение урона
        Примеры:
        >>> character = Character("John", 100, 100)
        >>> character.hit(30)
        """
        if not isinstance(damage, int):
            raise TypeError("Урон должен быть типа float")
        if damage < 0:
            raise ValueError("Урон не должен быть отрицательным")
        if self.armor - damage > self.max_hp:
            raise ValueError("Персонаж умер")

        self.hp = self.max_hp - (damage - self.armor)

    def healing_spell(self, heal: int, mana_cost: int):
        """
        Персонаж может скастовать лечебное заклинание и вылечиться
        :param heal: Восстановление здоровья
        :param mana_cost: Затраты маны
        :raise ValueError: Если полученное лечение больше максимального хп
        :raise ValueError: Если недостаточно маны
        :return: Ноове здоровье персонажа
        Примеры:
        >>> character = Character("John", 50, 50)
        >>> character.healing_spell(20,20)
        """
        if not isinstance(heal, int):
            raise TypeError("Востановление здоровья должно быть типа int")
        if not isinstance(mana_cost, int):
            raise TypeError("Затраты маны должны быть типа int")
        if heal < 0:
            raise ValueError("Востановленное здоровье быть не отрицательным числом")
        if self.hp + heal > self.max_hp:
            raise ValueError("Востановленное здоровье не может быть больше максимального здоровья")
        if self.mana - mana_cost < 0:
            raise ValueError("Недостаточно маны")
        self.hp += heal

        #Где-то вот здесь я прочитал что реализовать методы целиком не нужно

class Car:
    def __init__(self, speed: float, fuel: float):
        """
        Машина
        :param speed Скорость машины, теущая
        :param fuel Бензин в машине
        Примеры:
        >>> car = Car(80,200)  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость машины должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость должен быть положительным числом")
        if speed >= 200:
            raise ValueError("Скорость машины на трассе не может быть больше 120 км в час")
        self.speed = speed

        if not isinstance(fuel, (int, float)):
            raise TypeError("Количество бензино должно быть типа int или float")
        if fuel < 0:
            raise ValueError("Количество бензина не может быть отрицательным")
        self.fuel = fuel

    def empty_fueltank(self):
        """
        Функция которая проверяет заправлена ли машина
        :return Заправлена ли машина
        Примеры:
        >>> car = Car(80,0)
        """
        ...

    def breaks(self, breaks_pressed: bool):
        """
        Функцция которая которая тормозит машину
        :param breaks_pressed нажаты ли тормоза
        :raise TypeError: если нажатие тормозов не задано через bool
        :return нулевую скорость машины
        Примеры:
        >>> car = Car(80,80)
        >>> car.breaks(True)
        """
        if not isinstance(breaks_pressed, bool):
            raise TypeError("Тормоза могут быть только нажаты или не нажаты")
        ...


class Submachine_Gun:
    def __init__(self, DPS:float, range:float, ammo:float, hitrate:float):
        """
        Пистолет пулемет
        :param DPS - урон пистолет пулемёта в секунду
        :param range - прицельная дальность стрельбы
        :param ammo - количество патронов в обойме, максимальное
        :param hitrate - шанс попадания
        Примеры:
        >>> weapon = Submachine_Gun(20,100,24,100) #инициация экземпляра класса
        """
        self.special_values = DPS, range, ammo, hitrate
        for keys in self.special_values:
            if not isinstance(keys, (int, float)):
                raise TypeError("Параметры пистолет пулемета должны падаваться только через float")
            if keys < 0:
                raise ValueError("Параметры пистолет пуллемета не могут быть отрицательными")
        self.dps = DPS
        self.range = range
        self.ammo = ammo
        self.hitrate = hitrate


    def reload(self):
        """
        Функция которая перезаряжает пистолет пулемет
        :param текущее количество патронов
        :raise Value Error если магазин еще не опустел
        :return: Максимальное количество патронов + 1 в самом стволе
        """
        if self.ammo > 0:
            raise ValueError("Патроны еще не закончились")
        ...

    def damage_falloff(self, target_range: float):
        """
        Функция которая уменьшает урон с дистанцией по формуле DPS*(range/target_range
        :param target_range расстрояние до цели
        :raise ValueError если расстояние отрицательное
        :return: Уменьшенный урон
        """
        if not isinstance(target_range, (float,int)):
            raise TypeError("Расстояние до цели должно подаваться числом")
        if target_range < 0:
            raise ValueError("Расстояние до цели не может быть отрицательным")
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
