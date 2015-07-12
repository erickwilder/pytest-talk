# coding: utf-8

from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Home view', 200

    return app
