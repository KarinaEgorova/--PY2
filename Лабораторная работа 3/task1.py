class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property   # реализуем свойства, которые не позволят изменять атрибуты, а только вернут значения
    def name(self):
        return self._name

    @property  # атрибут также изменяться не может
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс Бумажные книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)   # вызываем конструктор базового класса и расширяем
        self._pages = pages

    @property   # реализуем метод pages и используем декоратор @property
    def pages(self) -> int:
        """Возвращаем количество страниц"""
        return self._pages

    @pages.setter  # реализуем метод pages и используем свойство setter
    def pages(self, new_pages: int) -> None:
        """Проверка допустимости входящих данных при присвоении значений атрибутам"""
        if not isinstance(new_pages, int):
            raise TypeError('Нумерация страниц должна быть типа int')
        if new_pages <= 0:
            raise ValueError('Нумерация страниц должна начинаться с 1')
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц {self.pages}"  # перегружаем str

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Дочерний класс Аудиокниги"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Возвращаем продолжительность книги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        """Проверка допустимости входящих данных при присвоении значений атрибутам"""
        if not isinstance(new_duration, float):
            raise TypeError('Продолжительность книги должна быть типа float')
        if new_duration <= 0.0:
            raise TypeError('Продолжительность книги должна быть положительной')
        self.duration = new_duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
