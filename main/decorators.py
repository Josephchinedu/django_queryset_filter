from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end_time - start_time):.2f}s")

        return result
    return inner