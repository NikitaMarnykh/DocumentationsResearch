from django.core.management.base import BaseCommand
from QuotesCentralBank.models import Quote
from QuotesCentralBank.services import get_quotes


# Заполняем базу данных котировоками
class Command(BaseCommand):
    help: str = "Инициализация котировок"

    def handle(self, *args, **options):
        quotes = get_quotes()
        if quotes is None:
            self.stdout.write("Инциализация котировок не удалась")
        else:
            Quote.objects.bulk_create(
                [Quote(**quote) for quote in quotes]
            )
            self.stdout.write("Инциализация котировок прошла успешно")

