from django.core.management.base import BaseCommand
from .cbdb_scraper import CBDBReviewScraper
from knihy.models import Book

class Command(BaseCommand):
    help = 'Scrape Books Review'

    for book in Book.objects.all():
        my_scraper = CBDBReviewScraper(book.ISBN)
        review = my_scraper.get_review()
        book.hodnoceni = review
        book.save()
    

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully ran my_custom_command'))