from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.paginator import Paginator
from speedtest.models import Customer
import uuid
import psutil
import time
from random import randint
import timeit

class Command(BaseCommand):
    help = 'orm speed test'

    def get_100_rec(self):
        customers = Customer.objects.filter()[:100]

    def count_rec(self):
        count = Customer.objects.count()

    def paginate_100_rec(self):
        customers = Customer.objects.all()
        paginator = Paginator(customers, 100)
        page = 1
        contacts = paginator.get_page(page)

    def aggregation(self):
        amount = Customer.objects.all().aggregate(Avg('amount'))

    def crate_rec(self):
        User.objects.create(
            username=uuid.uuid4(),
            first_name="speed_test_django"
        )

    def update_rec(self):
        user_name = "speed_test_django"
        user = User.objects.first()
        user.last_name=user_name
        user.save()

    def handle(self, *args, **options):
        rotation = 100
        print ("select:", timeit.Timer(self.get_100_rec).timeit(rotation))
        print ("count:", timeit.Timer(self.count_rec).timeit(rotation))
        print ("paginate_100_rec:", timeit.Timer(self.paginate_100_rec).timeit(rotation))
        print ("aggregation:", timeit.Timer(self.aggregation).timeit(rotation))
        print ("crate_rec:", timeit.Timer(self.crate_rec).timeit(rotation))
        print ("update_rec:", timeit.Timer(self.update_rec).timeit(rotation))