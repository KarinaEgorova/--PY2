import doctest


class Microscope:
    def __init__(self, brightness: int, magnification: int, focus: int):
        """
        Создание и подготовка к работе объекта "Микроскоп"
        :param brightness: освещенность Микроскопа в Люксах
        :param magnification: увеличение Микроскопа
        :param focus: Фокусное расстояние Микроскопа

        Пример:
        >>> microscope = Microscope(50000, 25, 400)  #Инициализация экземпляра класса
        """

        if not isinstance(brightness, int):
            raise TypeError('Освещенность микроскопа должно быть типа int')
        if brightness <= 0:
            raise ValueError('Освещенность микроскопа должна быть положительны числом')
        self.brightness = brightness

        if not isinstance(magnification, int):
            raise TypeError('Увеличение микроскопа должно быть типа int')
        if magnification <= 0:
            raise ValueError('Увеличение микроскопа должна быть положительны числом')
        self.magnification = magnification

        if not isinstance(focus, int):
            raise TypeError('Фокусное расстояние микроскопа должно быть типа int')
        if focus <= 0:
            raise ValueError('Фокусное расстояние микроскопа должна быть положительным числом')
        self.focus = focus

    def install_brightness_level(self, brightness_level) -> int:
        """

        :param brightness_level: устанавливаемый уровень яркости на микроскопе
        :raise ValueError: Если установленная яркость превышает максимально возможный уровень освещенности
        :return: Реально установленная яркость освещения микроскопа

        Примеры:
        >>> microscope = Microscope(50000, 25, 400)
        >>> microscope.install_brightness_level(50000)
        """
        if not isinstance(brightness_level, int):
            raise TypeError('Уровень яркости микроскопа должно быть типа int')
        if brightness_level <= 0:
            raise ValueError('Уровень яркости микроскопа должнен быть положительны числом')
        ...

    def install_magnification(self, magnification_changer) -> int:
        """

        :param magnification_changer: преобразователь, устанавливающий увеличение в микроскопе
        :raise ValueError: Если значение увеличения превышает максимально возможное
        :return: Реально установленное значение увеличения

        Примеры:
        >>> microscope = Microscope(50000, 25, 400)
        >>> microscope.install_magnification(16)
        """
        if not isinstance(magnification_changer, int):
            raise TypeError('Значение увеличения микроскопа должно быть типа int')
        if magnification_changer <= 0:
            raise ValueError('Значение увеличения микроскопа должно быть положительным числом')
        ...


if __name__ == "__main__":
    doctest.testmod()


class Piano:
    def __init__(self, color: str, keys: int, pedals: int):
        """

        :param color: Цвет пианино
        :param keys: Количество клавиш в клавиатуре
        :param pedals: Количество педалей

        Пример:
        >>> piano = Piano("brown", 88, 3)  # Инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError('Цвет пианино должен быть типа str')
        self.color = color

        if not isinstance(keys, int):
            raise TypeError('Количество клавиш в клавиатуре должно быть типа int')
        if keys <= 0:
            raise ValueError('Количество клавиш в клавиатуре должно быть положительным числом')
        self.keys = keys

        if not isinstance(pedals, int):
            raise TypeError('Количество педалей должно быть типа int')
        if pedals <= 0:
            raise ValueError('Количество педалей должно быть положительным числом')
        self.pedals = pedals

    def opening_cover(self) -> str:
        """
        Подготовка инструмента
        :return: "Preparing the instrument"
        """
        ...

    def playing_the_piano(self) -> str:
        """
        Игра на пианино
        :return: "I'm playing the piano"
        """
        ...


import doctest


class Printer:
    def __init__(self, printer_type: str, connection: str, paper_tray: int):
        """

        :param printer_type: тип принтера (лазерный, светодиодный...)
        :param connection: тип подключения к ПК
        :param paper_tray: наполненность бумагой

        Пример:
        >>> printer = Printer("Лазерный", "Проводное подключение", 100)  # Инициализация экземпляра классов
        """
        if not isinstance(printer_type, str):
            raise TypeError('Тип принтера должен быть типа str')
        self.printer_type = printer_type

        if not isinstance(connection, str):
            raise TypeError('Тип подключения должен быть типа str')
        self.connection = connection

        if not isinstance(paper_tray, int):
            raise TypeError('Наполненность бумагой должна быть типа int')
        if paper_tray < 0:
            raise ValueError('Наполненность бумагой должна быть положительным числом или 0')
        self.paper_tray = paper_tray

    def is_empty_paper_tray(self) -> bool:
        """
        Функция проверяет наполненность принтера бумагой
        :return: Является ли лоток для бумаги пустым

        Примеры:
        printer = Printer("Лазерный", "Проводное", 100)
        printer.is_empty_paper_tray()
        """
        ...

    def print_the_document(self, printed_paper: int) -> None:
        """

        :param printed_paper: количество печатаемых листов
        :raise ValueError: Если количество печатаемых листов превышает кол-во бумаги в принтере, вызвать ошибку
        Примеры:
        >>> printer = Printer("Лазерный", "Проводное", 100)
        >>> printer.print_the_document(100)
        """
        if not isinstance(printed_paper, int):
            raise TypeError('Количество печатаемых листов должно быть типа int')
        if printed_paper <= 0:
            raise ValueError('Количество печатаемых листов должно быть положительным числом')

        ...


if __name__ == "__main__":
    doctest.testmod()
