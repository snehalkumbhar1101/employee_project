"""Fixtures for flask."""

from functools import partial
from unittest.mock import MagicMock

from flask import g


def mock(monkeypatch, **kwargs):
    """Fix the flask global object.

    The “g” object on flask is throwing exception whenever you try to access
    properties on it (based on the fact that an application context is not
    yet available). Since we use the logger across our application, we don't
    want to write tests that have dependencies on flask. This fixture fixes
    this.

    Args:
        monkeypatch (MonkeyPatch): pytest monkeypatch.
        kwargs (dict): additional properties to mock.
    """
    get_attribute = partial(
        mock_flask_global_get_attribute, ows=MagicMock(), log=MagicMock(),
        **kwargs)
    monkeypatch.setattr(g.__class__, '__getattr__', get_attribute)


def mock_flask_global_get_attribute(name, **kwargs):
    """Get a specific attribute.

    Args:
        name (str): the name of the attribute.
        kwargs (dict): properties to mock.
    """
    return kwargs.get(name) or MagicMock()
