class Book:
    book_material = 'paper'
    text_presence = True


    def __init__(self, title, author, pages_amount, isbn, reserved):
        self.title = title
        self.author = author
        self.pages_amount = pages_amount
        self.isbn = isbn
        self.reserved = reserved


    def print_book_info(self):
        if self.reserved:
            print(
                f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.pages_amount}, материал: {self.book_material}, '
                'зарезервирована'
            )
        else:
            print(
                f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.pages_amount}, материал: {self.book_material}'
            )


class Schoolbook(Book):


    def __init__(
        self,
        title,
        author,
        pages_amount,
        isbn,
        reserved,
        subject,
        class_number,
        task_presence
    ):
        super().__init__(title, author, pages_amount, isbn, reserved)
        self.subject = subject
        self.class_number = class_number
        self.task_presence = task_presence


    def print_book_info(self):
        if self.reserved:
            print(
                f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.pages_amount}, предмет: {self.subject}, '
                f'класс: {self.class_number}, зарезервирована'
            )
        else:
            print(
                f'Название: {self.title}, Автор: {self.author}, '
                f'страниц: {self.pages_amount}, предмет: {self.subject}, '
                f'класс: {self.class_number}'
            )


book_1 = Book('Book1', 'author1', 123, 'ISBN', True)
book_2 = Book('Book2', 'author2', 456, 'ISBN', False)
book_3 = Book('Book3', 'author3', 789, 'ISBN', False)
book_4 = Book('Book4', 'author4', 789, 'ISBN', False)
book_5 = Book('Book5', 'author5', 789, 'ISBN', False)

school_book_1 = Schoolbook('Geometry', 'Ivanov', 143, 'ISBN', True, 'Geometry', 7, True)
school_book_2 = Schoolbook('Algebra', 'Sidorov', 643, 'ISBN', False, 'Algebra', 9, True)
school_book_3 = Schoolbook('History', 'King', 643, 'ISBN', False, 'History', 11, True)

Book.print_book_info(book_1)
Book.print_book_info(book_2)
Book.print_book_info(book_3)
Book.print_book_info(book_4)
Book.print_book_info(book_5)
Schoolbook.print_book_info(school_book_1)
Schoolbook.print_book_info(school_book_2)
Schoolbook.print_book_info(school_book_3)
