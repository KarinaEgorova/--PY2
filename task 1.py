import doctest


class Microscopes:
    """
          Базовый класс "Микроскопы"
          Создание и подготовка к работе объекта "Микроскоп"
          :param name: наименование Микроскопа по Регистрационному удостоверению
          :param form: тип Микроскопа (оптический, цифровой)
          :param brightness: освещенность Микроскопа в Люксах
          :param magnification: увеличение Микроскопа, кратность
          :param rotoplate: поворотное кольцо для Микроскопа
          """
    def __init__(self, name: str, form: str, brightness: int, magnification: int, rotoplate: str):
        self._name = name
        self._form = form
        self._brightness = brightness
        self._magnification = magnification
        self.rotoplate = rotoplate

    @property   # Атрибут name изменяться не может, данная информация от производителя
    def name(self):
        return self._name

    @property  # Атрибут type изменяться не может - данный параметр невозможен к изменению
    def form(self):
        return self._form

    @property
    # реализуем метод brightness
    # и используем декоратор @property
    def brightness(self) -> int:
        """Возвращаем яркость Микроскопа"""
        return self._brightness

    @brightness.setter
    # реализуем метод brightness
    # и используем свойство setter для присвоения значения яркости при регулировке
    def brightness(self, new_brightness: int) -> None:
        """Проверка допустимости входящих данных при присвоении значений атрибутам"""
        if not isinstance(new_brightness, int):
            raise TypeError('Устанавливаемая яркость должна быть типа int')
        if 0 <= new_brightness <= 120000:
            raise ValueError('Яркость может быть установлена в пределах значений [1,120000]')
        self._brightness = new_brightness

    @property
    # реализуем метод magnification
    # и используем декоратор @property
    def magnification(self) -> int:
        """Возвращаем увеличение Микроскопа"""
        return self._magnification

    @magnification.setter
    # реализуем метод magnification
    # и используем свойство setter для присвоения значения увеличения при регулировке
    def magnification(self, new_magnification: int) -> None:
        """Проверка допустимости входящих данных при присвоении значений атрибутам"""
        if not isinstance(new_magnification, int):
            raise TypeError('Устанавливаемое увеличение должно быть типа int')
        if 4 <= new_magnification <= 25:
            raise ValueError('Увеличение может быть установлено в пределах значений [4,25]')
        self._magnification = new_magnification

    def add_equipment(self):
        """Возвращаем дополнительный аксессуар для Микроскопа"""
        return self.rotoplate

    def __str__(self):
        return f"Микроскоп {self.name}. Тип {self.form}. Яркость {self.brightness}. Увеличение {self.magnification}. Поворотное кольцо {self.rotoplate}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, form={self.form!r}), brightness={self.brightness!r}, magnification={self.magnification!r}, rotoplate={self.rotoplate!r}"


class Colposcopes(Microscopes):
    """
    Дочерний класс "Кольпоскопы"
    Создание и подготовка к работе объекта "Кольпоскоп"
    Вызываем конструктор базового класса и расширяем его
    :param binocular_tube: угол наклона бинокулярного тубуса Кольпоскопа
    """
    def __init__(self, name: str, form: str, brightness: int, magnification: int, rotoplate: str, binocular_tube: int):
        super().__init__(name, form, brightness, magnification, rotoplate)
        self._binocular_tube = binocular_tube

    @property
    # реализуем метод binocular_tube
    # и используем декоратор @property
    # пользователю можно только получить данную информацию
    def binocular_tube(self) -> int:
        """Возвращаем значение угла наклона бинокулярного тубуса"""
        return self._binocular_tube

    """
    Перегружаем методы str и repr для переопределения логики класса
    """
    def __str__(self):
        return f"Микроскоп {self.name}. Тип {self.form}. Яркость {self.brightness}. Увеличение {self.magnification}. Поворотное кольцо {self.rotoplate}. Бинокулярный тубус {self._binocular_tube}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r},  form={self.form!r}), brightness={self.brightness!r}, magnification={self.magnification!r},rotoplate={self.rotoplate!r}, binocular_tube={self._binocular_tube!r}"


class StomMicroscopes(Microscopes):
    """
    Дочерний класс "Стоматологические микроскопы"
    Создание и подготовка к работе объекта "Стоматологический микроскоп"
    Вызываем конструктор базового класса и расширяем его
    :param varioscope: Объектив с изменяемым фокусным расстоянием
    :param irisdiafragm: ирисовая диафрагма для микроскопа (микрофокус)
    """
    def __init__(self, name: str, form: str, brightness: int, magnification: int, rotoplate: str, varioscope: int, irisdiafragm: str):
        super().__init__(name, form, brightness, magnification, rotoplate)
        self._varioscope = varioscope
        self.irisdiafragm = irisdiafragm

    @property
    # реализуем метод varioscope
    # и используем декоратор @property
    def varioscope(self) -> int:
        """Возвращаем фокусное расстояние Микроскопа"""
        return self._varioscope

    @varioscope.setter
    # реализуем метод varioscope
    # и используем свойство setter для присвоения значения яркости при регулировке
    def varioscope(self, install_varioscope: int) -> None:
        """Проверка допустимости входящих данных при присвоении значений атрибутам"""
        if not isinstance(install_varioscope, int):
            raise TypeError('Устанавливаемое фокусное расстояние должно быть типа int')
        if 200 <= install_varioscope <= 400:
            raise ValueError('Фокусное расстояние может быть установлено в пределах значений [200,400]')
        self._varioscope = install_varioscope

    def add_equipment(self):
        """
        Метод "Дополнительные акссесуары" переопределен с добавлением атрибута
        Для класса "Стоматологические микроскопы" также необходимо использовать атрибут - ирисовая диафрагма
        """
        super().add_equipment()
        return self.irisdiafragm

    """Перегружаем методы str и repr для переопределения логики класса"""
    def __str__(self):
        return f"Микроскоп стоматологический {self.name}. Тип {self.form}. Яркость {self.brightness}. Увеличение {self.magnification}. Вариоскоп {self.varioscope}. Ирисовая диафрагма {self.irisdiafragm}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, form={self.form!r}), brightness={self.brightness!r}, magnification={self.magnification!r},varioscope={self.varioscope!r}, irisdiafragm={self.irisdiafragm!r}"


if __name__ == "__main__":
    doctest.testmod()
    pass
