from flask import request
from flask_restplus import Resource
from .models import AuthUser, SpeedtestCustomer
from .schemas import CustomerSchema, UserSchema
from sqlalchemy import func
import random, math
from app import db
import uuid
from flask_script import Command
import timeit

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


class SimpleList(Resource):
    def get(self):
        data = DATA
        return data


class HeavyCodeList(Resource):
    def get(self):
        data = gibbs()
        return { "action": "done" }


class SelectList(Resource):
    def get(self):
        customers = SpeedtestCustomer.query.filter().limit(100)
        user_schema = CustomerSchema(many=True)
        return user_schema.dump(customers)


class Count(Resource):
    def get(self):
        count = SpeedtestCustomer.query.count()
        return { "count": count }


class PaginatedList(Resource):
    def get(self, page=1):
        per_page = 100
        customers = SpeedtestCustomer.query.filter().paginate(page,per_page,error_out=False)
        user_schema = CustomerSchema(many=True)
        return user_schema.dump(customers.items)


class Aggregation(Resource):
    def get(self):
        amount = db.session.query(func.avg(SpeedtestCustomer.amount))
        return {
            "amount": amount,
            "random": random.randint(10000,1000000)
        }


class Create(Resource):
    def post(self):
        user = AuthUser(
            username=str(uuid.uuid4()),
            first_name=str(request.json['first_name'])
        )
        db.session.add(user)
        db.session.commit()
        return {"created": True}


class Save(Resource):
    def put(self):
        user = AuthUser.query.filter_by().first()
        user.last_name = request.json['last_name'] 
        db.session.commit()
        return { "saved": True }

class Update(Resource):
    def put(self):
        user = AuthUser.query.filter_by(id=self.user_id).update(dict(last_name=request.json['last_name']))
        db.session.commit()
        return { "updated": True }


class OrmSpeedTest(Command):
    user_id = 1

    def get_100_rec(self):
        customers = SpeedtestCustomer.query.filter().limit(100)
    

    def count_rec(self):
        count = SpeedtestCustomer.query.count()

    
    def paginate_100_rec(self):
        per_page = 100
        page = 1
        customers = SpeedtestCustomer.query.filter().paginate(page,per_page,error_out=False)


    def aggregation(self):
        amount = SpeedtestCustomer.query.with_entities(func.avg(SpeedtestCustomer.amount))[0]

    def crate_rec(self):
        user = AuthUser(
            username=uuid.uuid4(),
            first_name="speed_test_flask"
        )
        db.session.add(user)
        db.session.commit()


    def save_rec(self):
        user = AuthUser.query.first()
        user.last_name = "speed_test_flask_7"
        db.session.merge(user)
        db.session.commit()

    
    def update_rec(self):
        user = AuthUser.query.filter_by(id=self.user_id).update(dict(last_name="speed_test_flask_5"))
        db.session.commit()
        

    def run(self):
        user = AuthUser.query.first()
        rotation = 1000
        self.user_id = user.id
        print ("select:", timeit.Timer(self.get_100_rec).timeit(rotation))
        print ("count:", timeit.Timer(self.count_rec).timeit(rotation))
        print ("paginate_100_rec:", timeit.Timer(self.paginate_100_rec).timeit(rotation))
        print ("aggregation:", timeit.Timer(self.aggregation).timeit(rotation))
        print ("crate_rec:", timeit.Timer(self.crate_rec).timeit(rotation))
        print ("save_rec:", timeit.Timer(self.save_rec).timeit(rotation))
        print ("update_rec:", timeit.Timer(self.update_rec).timeit(rotation))
