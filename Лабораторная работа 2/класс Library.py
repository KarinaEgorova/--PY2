BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages


class Library:
    def __init__(self, books=None):  # указываем значение по умолчанию None
        if books is None:
            books = []  # если не передано значение, то пустой список книг
        self.books = books  # инициализируем атрибут - список книг

    def get_next_book_id(self) -> int:  # метод для добавления новой книги в библиотеку
        if not self.books:  # если в библиотеке нет книг, возвращаем 1
            return 1
        return self.books[-1].id_ + 1  # последнюю книгу объявляем через [-1]

    def get_index_by_book_id(self, id_) -> int:  # метод по возвращению индекса книги в списке
        for i, book in enumerate(self.books):  # enumerate для возвращения индекс-значение
            if book.id_ == id_:  # если существует книга с запрашиваемым id, возвращаем её индекс
                return i
            else:
                raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
