from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.BaseConfiguration')

from app.snpp import views
