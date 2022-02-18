"""Test employee_info logic.

Tests for logic layer functions for employee information retrieval.
"""


from datetime import datetime
from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from flask_api import response
# from pymysql import constants
from sqlalchemy.engine import result


from employee_details.app import app
from employee_details.logic import employee_operation
from employee_details.models import employee_info
from validation import constants
from pytest_mock import mocker

@pytest.mark.parametrize(
    ('model_fn','model_fn_params',
     'expected_result','eid'), [
        (constants.EMPLOYEE_INFO_EMPLOYEE,None,'fetch_employee',None,
         ),
        (constants.EMPLOYEE_INFO_EMPLOYEE,[1],'fetch_employee',[1],
         ), ])
def test_get_employees(
         mocker, eid , model_fn, model_fn_params,
        expected_result, ):
    """Test successfully getting employee information."""

    mocker.patch.object(
        employee_info,'fetch_employee',
        return_value=response.Response(' employee'), autospec=True)

    result = employee_operation.get_employee(eid)
    getattr(employee_info.Employee,model_fn).assert_called_with(model_fn_params)
    assert result
    assert result.message == expected_result


@pytest.mark.parametrize(('employee_id', 'get_employees_result', 'expected_result'),[
    ('employee:2', response.Response(['employee']), response.Response('employee')),
    ('employee:2', response.Response([]),
     response.Response(status=404, message='employee not found.')),
    ('employee:2', response.Response(status=400),
     response.Response(status=400)),
])
def test_get_employee(mocker, employee_id, get_employees_result, expected_result):
    """Test get_employee."""
    mocker.patch.object(
        employee_info, 'get_employees', return_value=get_employees_result, autospec=True)

    employee_result = employee_operation.get_employee(employee_id)
    assert employee_result.status == expected_result.status
    assert employee_result.message == expected_result.message


