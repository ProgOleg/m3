from django.core.management.base import BaseCommand
from app.models import Port, Stock, Region, WholeSale, RetailSales


class Command(BaseCommand):

    @staticmethod
    def _regions() -> dict:
        regions_keys = {
            "lutsk": {"name": "Луцк", "stock": 1, "port": 0},
            "lviv": {"name": "Львов", "stock": 1, "port": 0},
            "uzhgorod": {"name": "Ужгород", "stock": 1, "port": 0},
            "ivano_frankivsk": {"name": "Ивано-Франковск", "stock": 1, "port": 0},
            "ternopil": {"name": "Тернополь", "stock": 1, "port": 0},
            "rivne": {"name": "Ровно", "stock": 2, "port": 0},
            "zhytomyr": {"name": "Житомир", "stock": 3, "port": 0},
            "khmelnitsky": {"name": "Хмельницкий", "stock": 2, "port": 0},
            "chernivtsi": {"name": "Черновцы", "stock": 1, "port": 0},
            "vinnytsia": {"name": "Винница", "stock": 2, "port": 0},
            "kiyv": {"name": "Киев", "stock": 4, "port": 0},
            "chernihiv": {"name": "Чернигов", "stock": 3, "port": 0},
            "sumy": {"name": "Сумы", "stock": 2, "port": 0},
            "poltava": {"name": "Полтава", "stock": 2, "port": 0},
            "cherkasy": {"name": "Черкасы", "stock": 2, "port": 0},
            "kropyvnytsky": {"name": "Кропивницкий", "stock": 2, "port": 0},
            "kharkov": {"name": "Харьков", "stock": 5, "port": 0},
            "donetsk": {"name": "Донецк", "stock": 0, "port": 0},
            "luhansk": {"name": "Луганск", "stock": 0, "port": 0},
            "dnieper": {"name": "Днепр", "stock": 3, "port": 3},
            "zaporizhzhia": {"name": "Запорожье", "stock": 4, "port": 2},
            "kherson": {"name": "Херсон", "stock": 3, "port": 3},
            "crimea": {"name": "Крым", "stock": 0, "port": 0},
            "nikolaev": {"name": "Николаев", "stock": 3, "port": 0},
            "odessa": {"name": "Одесса", "stock": 3, "port": 4}
            }
        return regions_keys

    def add_arguments(self, parser):
        # Positional arguments
        # parser.add_argument('poll_ids', nargs='+', type=int)

        # Named (optional) arguments
        parser.add_argument(
            '--sales_section',
            action='store_true',
            help='Populate db WholeSale and RetailSales models',
        )
        parser.add_argument(
            '--regions',
            action='store_true',
            help='Populate db WholeSale and RetailSales models',
        )

    def handle(self, *args, **options):
        if options.get("sales_section"):
            RetailSales.objects.create()
            WholeSale.objects.create()
        elif options.get("regions"):
            regions_keys = self._regions()
            for descripton, details in regions_keys.items():
                reg = Region.objects.create(name=details.get("name"), descripton=descripton, is_active=False)
                stock_count = details.get("stock")
                port_count = details.get("port")
                if stock_count:
                    for el in range(stock_count):
                        Stock.objects.create(region=reg)
                if port_count:
                    for el in range(port_count):
                        Port.objects.create(region=reg)
        print("Created")
