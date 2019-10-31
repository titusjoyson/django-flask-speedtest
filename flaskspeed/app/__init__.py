import logging

from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

import config
"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)

# database
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# namespace
from app.speedtest.controllers import api as speedtest_namespace

api = Api()

api.add_namespace(speedtest_namespace, path='/speedtest')

api.init_app(app)