# coding: utf-8
import pytest


@pytest.fixture(scope='session')
def session_app():
    from example.app import create_app
    return create_app()


@pytest.yield_fixture
def app(session_app):
    ctx = session_app.test_request_context()
    ctx.push()
    yield session_app
    ctx.pop()
