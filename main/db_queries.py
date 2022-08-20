import logging

from django.db.models import Prefetch
from main.decorators import query_debugger
from main.models import Publisher, Book, Store


@query_debugger
def book_list():

    """
    The decorstor will print the number of queries and the time it took to execute the query.

    One query for populating all the books and, while iterating each time, we access the foreign key publisher that another separate query executes.

    """

    queryset = Book.objects.all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})

    """
    Print Response:
        Function : book_list
        Number of Queries : 101
        Finished in : 0.06s
    """
    
    return books


@query_debugger
def book_list_select_related():

    """
    The decorstor will print the number of queries and the time it took to execute the query.

    This function is the modification of the book_list function.

    """
    queryset = Book.objects.select_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name, 'publisher': book.publisher.name})


    """
    Print Response:
        Function : book_list_select_related
        Number of Queries : 1
        Finished in : 0.01s 
    """

    return books


@query_debugger
def store_list():

    queryset = Store.objects.all()

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    
    """
    Print Response:
        Function : store_list
        Number of Queries : 11
        Finished in : 0.01s 
    """


    """
    We have 10 stores in the database and each store has 10 books. What's happening here is one query for fetching all the stores and, while iterating through each store, another query is executing when we access the ManyToMany field books.

    """

    return stores


@query_debugger
def store_list_prefetch_related():

    queryset = Store.objects.prefetch_related('books')

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    
    """
    Print Response:
        Function : store_list_prefetch_related
        Number of Queries : 2
        Finished in : 0.00s  
    
    """

    return stores

    
