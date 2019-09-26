from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models import Count
from django.contrib.auth.models import User
import random, math
import uuid

DATA = [
            {
                "id": 1,
                "name": "260861f4-1008-49d3-87ef-dbd32b78fae7",
                "amount": 958603672,
                "user": {
                    "id": 27160,
                    "username": "260861f4-1008-49d3-87ef-dbd32b78fae7",
                    "email": "260861f4-1008-49d3-87ef-dbd32b78fae7"
                }
            },
            {
                "id": 2,
                "name": "e38b4cdc-b2c9-4452-a9ed-c326c2e7f998",
                "amount": 505838560,
                "user": {
                    "id": 27161,
                    "username": "e38b4cdc-b2c9-4452-a9ed-c326c2e7f998",
                    "email": "e38b4cdc-b2c9-4452-a9ed-c326c2e7f998"
                }
            },
            {
                "id": 3,
                "name": "f6d80e74-e340-49c3-a40b-02d7f1c7f874",
                "amount": 590426501,
                "user": {
                    "id": 27162,
                    "username": "f6d80e74-e340-49c3-a40b-02d7f1c7f874",
                    "email": "f6d80e74-e340-49c3-a40b-02d7f1c7f874"
                }
            },
            {
                "id": 4,
                "name": "72188cda-2901-4e8c-92d2-f6a78a74cb1c",
                "amount": 733092617,
                "user": {
                    "id": 27163,
                    "username": "72188cda-2901-4e8c-92d2-f6a78a74cb1c",
                    "email": "72188cda-2901-4e8c-92d2-f6a78a74cb1c"
                }
            },
            {
                "id": 5,
                "name": "4c6f778b-8f16-489c-bb52-4bea615af711",
                "amount": 395133510,
                "user": {
                    "id": 27164,
                    "username": "4c6f778b-8f16-489c-bb52-4bea615af711",
                    "email": "4c6f778b-8f16-489c-bb52-4bea615af711"
                }
            },
            {
                "id": 6,
                "name": "2d89c7fc-5ebd-4e63-aaea-086b254a9b1a",
                "amount": 4636042,
                "user": {
                    "id": 27165,
                    "username": "2d89c7fc-5ebd-4e63-aaea-086b254a9b1a",
                    "email": "2d89c7fc-5ebd-4e63-aaea-086b254a9b1a"
                }
            },
            {
                "id": 7,
                "name": "89660999-f64a-4318-b001-696c2fbf7bdb",
                "amount": 644680468,
                "user": {
                    "id": 27166,
                    "username": "89660999-f64a-4318-b001-696c2fbf7bdb",
                    "email": "89660999-f64a-4318-b001-696c2fbf7bdb"
                }
            },
            {
                "id": 8,
                "name": "a4e5c979-f15c-48fe-b3d5-2885af25e39f",
                "amount": 210861397,
                "user": {
                    "id": 27167,
                    "username": "a4e5c979-f15c-48fe-b3d5-2885af25e39f",
                    "email": "a4e5c979-f15c-48fe-b3d5-2885af25e39f"
                }
            },
            {
                "id": 9,
                "name": "1e95646c-db4b-4465-888a-dd832cfef84c",
                "amount": 306301242,
                "user": {
                    "id": 27168,
                    "username": "1e95646c-db4b-4465-888a-dd832cfef84c",
                    "email": "1e95646c-db4b-4465-888a-dd832cfef84c"
                }
            },
            {
                "id": 10,
                "name": "ebbd06c9-a33b-44e1-9736-8ff2d1ac868d",
                "amount": 890229987,
                "user": {
                    "id": 27169,
                    "username": "ebbd06c9-a33b-44e1-9736-8ff2d1ac868d",
                    "email": "ebbd06c9-a33b-44e1-9736-8ff2d1ac868d"
                }
            }
        ]

def gibbs(N=100, thin=100):
    x = 0
    y = 0
    for i in range(N):
        for j in range(thin):
            x = random.gammavariate(3, 1.0 / (y * y + 4))
            y = random.gauss(1.0 / (x + 1), 1.0 / math.sqrt(2 * x + 2))


class SimpleList(APIView):
    def get(self, request, format=None):
        data = DATA
        return Response(data)


class HeavyCodeList(APIView):
    def get(self, request, format=None):
        gibbs()
        return Response({ "action": "done" })


class SelectList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.filter()[:100]
        serializer = CustomerSerializer(customers, many=True)
        data = serializer.data
        return Response(data)


class CountList(APIView):
    def get(self, request, format=None):
        count = Customer.objects.count()
        return Response({ "count": count })


class PaginatedList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        paginator = Paginator(customers, 100)
        page = request.GET.get('page', 1)
        contacts = paginator.get_page(page)
        serializer = CustomerSerializer(contacts, many=True)
        data = serializer.data
        return Response(data)


class Aggregation(APIView):
    def get(self, request, format=None):
        amount = Customer.objects.all().aggregate(Avg('amount'))
        return Response({
            "amount": amount,
            "random": random.randint(10000,1000000)
        })


class Create(APIView):
    def post(self, request, format=None):
        User.objects.create(
            username=uuid.uuid4(),
            first_name=request.data['first_name']
        )
        return Response({"created": True})


class Update(APIView):
    def put(self, request, format=None):
        user = User.objects.first()
        user.last_name=request.data['last_name']
        user.save()
        return Response({"updated": True})


simple_list_view = SimpleList.as_view()
algo_view = HeavyCodeList.as_view()
select_list_view = SelectList.as_view()
count_list_view = CountList.as_view()
paginated_list_view = PaginatedList.as_view()
aggregation_list_view = Aggregation.as_view()
create_view = Create.as_view()
update_view = Update.as_view()