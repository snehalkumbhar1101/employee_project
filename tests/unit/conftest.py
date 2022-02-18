"""Test configuration."""
from unittest.mock import MagicMock
import pytest


import pytest
from node.base import Node

from employee_details import app


class Graph:
    pass


Graph.driver = MagicMock()
Graph.driver.side_effect = [MagicMock(), MagicMock()]

# GraphDatabase.driver = MagicMock()
# GraphDatabase.driver.side_effect = [MagicMock(), MagicMock()]
@pytest.fixture
def context():
    """Return flask app context, including a mock logger.

    Returns:
        AppContext: flask app context, including a mock logger.

    """
    # Import 'application' here because in ows-users it does a bunch of
    # auth-related imports and breaks this fixture.
    import application
    class MockLog:
        """Mock Logging Class."""

        def error(self):
            pass

        def info(self):
            pass

        def warning(self):
            pass

    context_instance = application.app.app_context()
    # context_instance.g.employee=flask_logger.employee()
    context_instance.g.employee.log = MockLog

    return context_instance

@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""
    return app.app.test_client()

@pytest.fixture
def employee_data():
    """Return employee data."""
    return {
        'items': [
            {
                'emp_id': 2,
                'emp_name': 'asmita',
                'emp_email': 'asmitagade',
                'active': 'Y',
            }
        ],
        'pagination': {
            'type': 'standard',
            'count': 1,
            'page_offset': 0,
            'page_limit': 50
        }
    }


@pytest.fixture
def employee_data_model():
    """Return employee data model."""
    return {
        'items': [
            {
                'emp_id': 2,
                'emp_name': 'name',
                'emp_email': 'email',
                'is_active': 'Y',
            }
        ],
        'pagination': {
            'type': 'standard',
            'count': 1,
            'page_offset': None,
            'page_limit': None
        }
    }


@pytest.fixture
def make_graph_node():
    """Node generating factory as fixture to create Node objects."""
    graph = Graph()

    def _make_node(node_id, labels=(), data={}):
        data['id'] = node_id
        obj = Node(graph, node_id, labels, data)
        return obj


    return _make_node








