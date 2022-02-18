"""Test user_info model.

Tests for functions working with AR DB records in the table 'orchadmin_users'.
"""
import employee as employee
import pytest


from employee_details.models import employee_info
from employee_details.models.employee_info import Employee
from validation import constants
@pytest.mark.parametrize(('employee_id', 'expected_result'),[
    (
        None,
        [
            employee.build(employee_id=1).to_dict(),
            employee.build(employee_id=2).to_dict()
        ]
    ),
    ([],[]),
     ([1],[employee.build(employee_id=1).to_dict()])
])
@pytest.test_schema
def test_fetch_employee(context,eid,expected_result):
    """Test fetch_oa_users."""
    pytest.seed_models(Employee.build(employee_id=1))
    pytest.seed_models(Employee.build(employee_id=2))
    with context:
        result=employee_info.fetch_employee(eid)
    assert result.message == expected_result
