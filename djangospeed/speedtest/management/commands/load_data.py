from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from speedtest.models import Customer
import uuid
import psutil
import time
from random import randint

class Command(BaseCommand):
    help = 'insert 100000 records in to database'

    def add_arguments(self, parser):
        parser.add_argument('rounds', type=int, help='Indicates the number of users rows to insert in db')

    def handle(self, *args, **options):
        rounds = options.get('rounds', 100000)
        users = []
        self.stdout.write("generating user object")
        user_ids = list(User.objects.values_list('id', flat=True))
        for id_n in range(1, rounds + 1):
            username = uuid.uuid4()
            user = User(
                username=username,
                email=username
            )
            
            users.append(user)
            user_len = len(users)
            if (user_len == 100000 or (rounds <= user_len and rounds == user_len)):
                self.stdout.write("inserting user %s" %user_len)
                User.objects.bulk_create(users)
                users = []
        
        self.stdout.write("generating customer")
        customers = []
        base_user = User.objects.filter().exclude(id__in=user_ids)
        base_user_count = User.objects.filter().exclude(id__in=user_ids).count()
        for user in base_user:
            customer = Customer(
                user=user,
                name=user.username,
                amount=randint(10000, 1000000000)
            )
            customers.append(customer)
            cus_len = len(customers)
            if (cus_len == 100000 or (base_user_count <= cus_len and base_user_count == cus_len)):
                self.stdout.write("inserting customers %s" % cus_len)
                Customer.objects.bulk_create(customers)
                customers = []

        self.stdout.write(self.style.SUCCESS('Successfully %s records inserted' % rounds))