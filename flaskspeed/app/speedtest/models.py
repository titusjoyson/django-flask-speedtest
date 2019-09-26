# coding: utf-8
from app import db
import datetime

class AuthUser(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128), nullable=False, default="")
    last_login = db.Column(db.DateTime(True))
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False, default="")
    last_name = db.Column(db.String(150), nullable=False, default="")
    email = db.Column(db.String(254), nullable=False, default="")
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_joined = db.Column(db.DateTime(True), nullable=False, default=datetime.datetime.now())


class SpeedtestCustomer(db.Model):
    __tablename__ = 'speedtest_customer'

    id = db.Column(db.Integer, primary_key=True, default=db.Text("nextval('speedtest_customer_id_seq'::regclass)"))
    name = db.Column(db.String(400))
    amount = db.Column(db.Float(53), nullable=False)
    user_id = db.Column(db.ForeignKey('auth_user.id', deferrable=True, initially='DEFERRED'), nullable=False, unique=True)

    user = db.relationship('AuthUser', uselist=False)
