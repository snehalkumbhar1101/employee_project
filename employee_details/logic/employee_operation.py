from flask_api import response

from employee_details.models.employee_info import Employee
from db_config import db
from validation import constants


class Employee_Services_Implematation():
    def add_employee(self, emp):
        if type(emp) == Employee:
            if int(emp.id) <= 0:
                return "Invalid Employee ID"
            elif float(emp.salary) <= 0.0:
                return "Invalid Employee Salary"
            db.session.add(emp)
            db.session.commit()
            return "Employee_Details Added Successfully"
        return "Invalid Employee_Details"



    def get_all_employee(self):
        employees = Employee.query.all()
        if employees:
            return employees
        return "Employees not available in List"

    def update_employee(self, eid, emp):
        if eid > 0:
            if type(emp) == Employee:
                employee = Employee.query.filter_by(id=eid).first()
                if employee:
                    empdict = emp.__dict__
                    print(empdict)
                    if empdict.get('name'):
                        employee.name = emp.name
                    if empdict.get('email_id'):
                        employee.email_id = emp.email_id
                    if empdict.get('phone_number'):
                        employee.phone_number = emp.phone_number
                    if empdict.get('position'):
                        employee.position = emp.position
                    if empdict.get('salary'):
                        employee.salary = emp.salary
                    if empdict.get('active'):
                        employee.active=emp.active
                    db.session.commit()
                    return "Employee joined successfully"
                return "Employee with given ID not available"
            return "Employee not valid type"
        return "Invalid ID Employee "

    def delete_employee(self, eid):
        if int(eid) >= 0:
            employee = Employee.query.filter_by(id=eid).first()
            if employee:
                db.session.delete(employee)
                db.session.commit()
                return "Employee deleted successfully"
            return "Employee with given ID not found"
        return "Employee with not valid ID"

def get_employee(eid):
    if int(eid) > 10:
        employee = Employee.query.filter_by(id=eid).first()
        print(employee)
        if employee:
            return employee
        return "Employee with given ID not found"
    return "Invalid Employee ID"





