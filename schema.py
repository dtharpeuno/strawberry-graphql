import typing
import strawberry


@strawberry.type
class Book:
    title: str
    author: str


current_books = []
def get_books():
    current_books.append(Book(
            title="The Great Gasby",
            author="F.Scott"
        ))
    return current_books


def get_books_for_author(root) -> typing.List[Book]:
    return [Book(title="Jurassic Park")]

@strawberry.type
class Author:
    name: str
    books: typing.List[Book]
    # books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book: 
        book = Book(
                title=title,
                author=author
            )
        current_books.append(book)
        print(current_books)
        return 
    
    @strawberry.mutation
    def add_author(self, name: str, books: typing.List[str]) -> Author: 
        for book in books:
            Book(
                title=book,
                author=name
            )

        author = Author(
                name=name,
                books=books
            )
        return author

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    authors: typing.List[Author] = strawberry.field(resolver=get_books_for_author)


schema = strawberry.Schema(query=Query, mutation=Mutation)
