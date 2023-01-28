class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Недопустимое название")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Недопустимое значение")
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages_value: int):
        if not isinstance(new_pages_value, int):
            raise TypeError("Недопустимое значение")
        if new_pages_value < 0:
            raise ValueError("Недопустимое значение")
        self._pages = new_pages_value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration_value: float):
        if not isinstance(new_duration_value, float):
            raise TypeError("Недопустимое значение")
        if new_duration_value < 0:
            raise ValueError("Недопустимое значение")
        self._duration = new_duration_value

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность: {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
