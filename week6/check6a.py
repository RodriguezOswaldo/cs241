class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publication_year = None

    def prompt_book_info(self):
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = int(input('Publication Year: '))

    def display_book_info(self):
        print(f'{self.title} ({self.publication_year}) by {self.author}')


class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ''

    def prompt_subject(self):
        self.subject = input('Subject:')

    def display_subject(self):
        print(f'Subject: {self.subject}')


class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ''

    def prompt_illustrator(self):
        self.illustrator = input('Illustrator:')

    def display_illustrator(self):
        print(f'Illustrator: {self.illustrator}')


mybook = TextBook()
mybook.prompt_book_info()
mybook.prompt_subject()
mybook.display_book_info()
mybook.display_subject()
