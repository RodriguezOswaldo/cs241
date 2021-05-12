# def green(msj):
#     return "\033[0;32m{0}\033[0m".format(msj)


class Person:

    def __init__(self, name="anonymous", by="unknown"):
        self.name = name
        self.birth_year = by

    def display(self):
        return f'{self.name} (b. {str(self.birth_year)})'


class Book:

    def __init__(self, author, title="untitled", publisher="unpublished"):
        self.author = author
        self.title = title
        self.publisher = publisher

    def display_book(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        print(f'{self.author.display()}')


def main():
    person = Person()
    book = Book(author=person)
    book.display_book()
    print()
    print("Please enter the following:")
    person.name = input('Name: ')
    person.birth_year = int(input('Year: '))
    book.title = input('Title: ')
    book.publisher = input('Publisher: ')
    print()

    book.display_book()


if __name__ == "__main__":
    main()
