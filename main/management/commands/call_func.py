from django.core.management import BaseCommand

from main.db_queries import book_list,book_list_select_related,store_list, store_list_prefetch_related


class Command(BaseCommand):
    help = "BASE COMMAND HELPER FOR TESTING DB QUERIES"

    def handle(self, *args, **options):
        # book_list()

        # book_list_select_related()

        # store_list()

        store_list_prefetch_related()