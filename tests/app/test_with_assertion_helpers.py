# coding: utf-8

import pytest


def assert_has_config(app, config_key):

    __tracebackhide__ = True

    if config_key not in app.config:
        found_keys = '\n'.join('- {}'.format(key) for key in app.config.keys())
        pytest.fail('"{}" config key not found. Found this instead:\n'
                    '{}'.format(config_key, found_keys))


def test_config_with_helper(app):
    assert_has_config(app, 'SQLALCHEMY_DATABASE_URI')
