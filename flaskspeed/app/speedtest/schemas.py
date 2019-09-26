from app import app
from .models import AuthUser, SpeedtestCustomer

from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class UserSchema(ma.TableSchema):
    class Meta:
        model = AuthUser
        fields = ("id", "username", "email")


class CustomerSchema(ma.TableSchema):
    user = ma.Nested(UserSchema)

    class Meta:
        model = SpeedtestCustomer
        fields = ("id", "name", "amount", 'user')