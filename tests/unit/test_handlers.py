import pytest
import json
import pytest

from flask_api import response
from pytest_mock import mocker

from tests.unit.conftest import fixture_client
from employee_details.logic import employee_operation
from employee_details.models import employee_info
from validation import constants

"""
****GET****
===============
"""

@pytest.mark.parametrize(
    'employees, expected_result, expected_status_code',
    (
            (
                     ({"ak":1},{"asmita":2},),

                     {'items': [{"ak":1}, {"asmita":2}]},
                     200,
            ),
            (
                    ({"ak":1},{"asmita":2},),

                    {
                        'code': constants.UNSUPPORTED_EMPLOYEE_CODE,
                        'message': constants.UNSUPPORTED_EMPLOYEE

                    },
                200,
            ),

         )
    )

def test_get_employees(
       employees,expected_result, expected_status_code,
        fixture_client,mocker, employee=None):
    """Test 'GET /employees' handler."""
    get_employees_mock = mocker.patch(
        'employee_details.logic.employee_operation.get_employees')
    get_employees_mock.return_value = response.Response(message=employee)

    handler_response = fixture_client.get('/employees?{param}={value}'.format(
        param=constants.QUERY_PARAM_EMPLOYEE, value=employee))
    result = json.loads(handler_response.data.decode())

    assert handler_response.status_code == expected_status_code
    assert result == expected_result




"""
****PUT****
===============
"""

@pytest.mark.parametrize(
    (
    'data',
    'headers',
    'get_attributes_response',
    'expected_response'),
    (
   # ok
    (
        {'active': 'Y'},
        {
            'Content-Type': 'application/json',
        },
        response.Response(
            message={
                'eid': 'employee:',
            }),
        response.Response()
    ),


    # missing `active` from json body
    (
        {'test': 'Y'},
        {
            'Content-Type': 'application/json',
        },
        response.Response(
            message={
                'eid': 'employee:',
            }),
        response.Response(
            status=400,
            ),
    )

    ))
def test_update_employee(
    data,
    headers,
    get_attributes_response,
    expected_response,
    fixture_client,mocker):
    """Test PUT /employees/<employee_id>/status handler."""

    mocker.patch.object(
        return_value=response.Response())
    mocker.patch.object(
        employee_info,'update_employee_status',
        return_value=expected_response)

    handler_response = fixture_client.put(
        '/employees/status', json=data, headers=headers)

    assert handler_response.status_code == expected_response.status















"""
****POST****
============
"""
@pytest.mark.parametrize((
    'employee_id',
    'add_profile_to_identity_response',
    'expected_status_code',
    'expected_result_data'
), (
    # 200 ok
    (
        '123456789abcdefghijklm',
        12345,
        'InsightsProfile',
        response.Response(),
        200,
        None
    ),
    # 400 validation error
    (
        '12345abc',
        12345,
        'InsightsProfile',
        None,
        400,
        {
            'code': 'validation_error',
            'message': {
                'identity_id': ['Length must be between 22 and 36.']
            }
        }
    ),
))
def test_add_profile_to_identity(
        mocker,
        fixture_client,
        eid,
        add_employee_response,
        expected_status_code,
        expected_result_data):
    """Test 'POST /employee/<employee_id>/<int:employee_id>' handler."""
    add_employee_mock = mocker.patch(
        'employee_details.logic.employee_operation.add_employee')
    add_employee_mock.return_value = \
        add_employee_response

    handler_response = fixture_client.post(
        (
            '/employee_operation/{EMPLOYEE_ID}').format(
            EMPLOYEE_ID=eid))
    result_data = None
    if handler_response.data.decode() != '':
        result_data = json.loads(handler_response.data.decode())
    if add_employee_response is not None:
        add_employee_mock.assert_called
        add_employee_mock.assert_called_with(
            eid)
    assert handler_response.status_code == expected_status_code
    assert result_data == expected_result_data














"""
****DELETE****
===============
"""


@pytest.mark.parametrize((

        'eid',
        'delete_employee_to_identity_response',
        'expected_status_code',
        'expected_result_data'
), (

        (
                '2',
                response.Response(),
                200,
                None
        ),
        (
                '2',
                None,
                400,
                {
                    'code': 'validation_error'}


        ),
))
def test_delete_handler(

        fixture_client,
        eid,
        delete_employee_to_identity_response,
        expected_status_code,
        expected_result_data, add_employee_mock=None, add_employee_response=None):
    ''' Test 'DELETE /employee/<int:employee_id>' handler.'''

    handler_response = fixture_client.delete(
        (
            '/employee_operation/{EMPLOYEE_ID}').format(
                EMPLOYEE_ID=eid))
    result_data = None
    if handler_response.data.decode() != '':
        result_data = json.loads(handler_response.data.decode())
    if add_employee_response is not None:
        add_employee_mock.assert_called
        add_employee_mock.assert_called_with(
            eid)
    assert handler_response.status_code == expected_status_code
    assert result_data == expected_result_data




