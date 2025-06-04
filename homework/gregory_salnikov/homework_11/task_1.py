class Book:
    page_material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def get_info(self):
        info = f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.page_material}"
        if self.reserved:
            info += ", зарезервирована"
        return info


book1 = Book("Идиот", "Достоевский", 500, "978-5-17-067580-5")
book2 = Book("Мастер и Маргарита", "Булгаков", 384, "978-5-17-067581-2")
book3 = Book("1984", "Оруэлл", 328, "978-5-17-067582-9")
book4 = Book("Преступление и наказание", "Достоевский", 608, "978-5-17-067583-6")
book5 = Book("Война и мир", "Толстой", 1225, "978-5-17-067584-3")

book3.reserved = True

for book in [book1, book2, book3, book4, book5]:
    print(book.get_info())

class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, grade, has_exercises, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def get_info(self):
        info = f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, предмет: {self.subject}, класс: {self.grade}"
        if self.reserved:
            info += ", зарезервирована"
        return info


textbook1 = SchoolBook("Алгебра", "Иванов", 200, "978-5-12345-678-9", "Математика", 9, True)
textbook2 = SchoolBook("История России", "Петров", 300, "978-5-12345-679-6", "История", 10, True)
textbook3 = SchoolBook("География", "Сидоров", 250, "978-5-12345-680-2", "География", 8, False)
textbook4 = SchoolBook("Физика", "Фролов", 350, "978-5-12345-681-9", "Физика", 11, True)
textbook5 = SchoolBook("Биология", "Козлова", 280, "978-5-12345-682-6", "Биология", 7, False)

textbook2.reserved = True

for textbook in [textbook1, textbook2, textbook3, textbook4, textbook5]:
    print(textbook.get_info())