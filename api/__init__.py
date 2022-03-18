from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import Config


class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.api = Api(self.app)
        self.db = SQLAlchemy(self.app)

    def run(self):
        self.app.run(debug=True)

server = Server()
