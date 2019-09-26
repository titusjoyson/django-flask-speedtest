from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from speedtest.models import Customer
import uuid
import psutil
import time
from random import randint

class Command(BaseCommand):
    help = 'insert 1000000 records in to database'

    def handle(self, *args, **options):
        users = []
        self.stdout.write("generating user object")
        for id_n in range(1, 1000001):
            username = uuid.uuid4()
            user = User(
                username=username,
                email=username
            )
            
            users.append(user)
            if (id_n % 100000 == 0):
                self.stdout.write("inserting user %s" % len(users))
                User.objects.bulk_create(users)
                users = []
        
        self.stdout.write("generating gustomer")
        customers = []
        for user in User.objects.all():
            customer = Customer(
                user=user,
                name=user.username,
                amount=randint(10000, 1000000000)
            )
            customers.append(customer)
            if (user.id % 100000 == 0):
                self.stdout.write("inserting customers %s" % len(customers))
                Customer.objects.bulk_create(customers)
                customers = []

        self.stdout.write(self.style.SUCCESS('Successfully 1000000 records inserted'))