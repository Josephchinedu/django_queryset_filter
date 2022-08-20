import random
from django.core.management.base import BaseCommand
from main.models import Publisher, Book, Store



class Command(BaseCommand):

    help = """
        This command is for inserting Publisher, Book, Store into database.
        Insert 5 Publishers, 100 Books, 10 Stores
        """

    

    def handle(self, *args, **options):
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # create 5 publishers
        publishers = [Publisher(name=f'Publisher {i}') for i in range(1, 6)]
        Publisher.objects.bulk_create(publishers)

        # create 20 books for every publisher
        counter = 0
        books = []

        for publisher in Publisher.objects.all():
            for i in range(20):
                books.append(Book(name=f'Book {counter}', price=random.randint(1, 100), publisher=publisher))
                counter += 1

        Book.objects.bulk_create(books)


        # create 10 stores and insert 10 books for every store
        books = [book for book in Book.objects.all()]
        print(books)
        for i in range(10):
            temp_books = books.pop()
            print(books)
            print(temp_books)
            store = Store.objects.create(name=f'Store {i + 1}')
            store.books.add(temp_books)
            store.save()

