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
        print(f'\n{self.title} ({self.publication_year}) by {self.author}')


class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ''

    def prompt_subject(self):
        self.subject = input('Subject: ')

    def display_subject(self):
        print(f'Subject: {self.subject}')


class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ''

    def prompt_illustrator(self):
        self.illustrator = input('Illustrator: ')

    def display_illustrator(self):
        print(f'Illustrated by {self.illustrator}')


def main():
    mybook = Book()
    mybook.prompt_book_info()
    mybook.display_book_info()
    print()
    my_textbook = TextBook()
    my_textbook.prompt_book_info()
    my_textbook.prompt_subject()
    my_textbook.display_book_info()
    my_textbook.display_subject()
    print()
    illustrator = PictureBook()
    illustrator.prompt_book_info()
    illustrator.prompt_illustrator()
    illustrator.display_book_info()
    illustrator.display_illustrator()


if __name__ == "__main__":
    main()
