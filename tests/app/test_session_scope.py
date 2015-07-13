# coding: utf-8

from flask import url_for


def test_requires_app_context(app):
    url_for('.home') == '/'


def test_config(app):
    assert 'SQLALCHEMY_DATABASE_URI' in app.config
