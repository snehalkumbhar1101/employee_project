import json
from db_config import db
from flask import request
from application import app
from employee_details.logic.employee_operation import Employee_Services_Implematation
from employee_details.app import app
from employee_details.models.employee_info import Employee
service = Employee_Services_Implematation()


@app.route('/hello/')
def hello():
    return "\n WELCOME..\nYour First Project"






@app.route('/employee/', methods=['POST'])
def add_employee():
    json_data = request.form
    if json_data:
        emp = Employee(id=json_data.get('Employee_Id'),
                       name=json_data.get('Employee_Name'),
                       email_id=json_data.get('Employee_email_id'),
                       phone_number=json_data.get('Employee_phone_number'),
                       position=json_data.get('Employee_position'),
                       salary=json_data.get('Employee_salary'),
                       joined_date=json_data.get('Employee_joined_date'),
                       active=json_data.get('Employee_activate'))
        
        msg = service.add_employee(emp)
        if "Added" in msg:
            return json.dumps({'Success': msg})
        else:
            return json.dumps({'Error': msg})
    return json.dumps({'Error': 'Employee fields can not be Empty'})

@app.route('/employee/<int:eid>', methods=['GET'])
def get_employee(eid):
    employee = service.get_employee(eid)
    if type(employee) == str:
        return json.dumps({"Error": employee})
    employee_dict = {'Employee_Id': employee.id,
                     'Employee_Name': employee.name,
                     'Employee_Email_Id':employee.email_id,
                     'Employee_Phone_Number':employee.phone_number,
                     'Employee_Position':employee.position,
                     'Employee_Salary': employee.salary}
    return json.dumps(employee_dict)

@app.route('/employee/', methods=['GET'])
def get_all_employee():
    employees = service.get_all_employee()
    if type(employees) == str:
        return json.dumps({'Error': employees})
    employees_list = []
    for employee in employees:
        employee_dict = {'Employee_Id': employee.id,
                         'Employee_Name': employee.name,
                         'Employee_Email_Id': employee.email_id,
                         'Employee_Phone_Number':employee.phone_number,
                         'Employee_Position':employee.position,
                         'Employee_Salary':employee.salary}
        employees_list.append(employee_dict)
    return json.dumps(employees_list)


@app.route('/employee/<int:eid>', methods=['PUT'])
def update_employee(eid):
    json_data = request.form
    print(json_data)
    print(json_data.get('Employee_name'))
    if json_data:
        emp = Employee(id=eid,
                       name=json_data.get('Employee_Name'),
                       email_id=json_data.get('Employee_email_id'),
                       phone_number=json_data.get('Employee_phone_number'),
                       position=json_data.get('Employee_position'),
                       salary=json_data.get('Employee_salary'),
                       joined_date=json_data.get('Employee_joined_date'),
                       active=json_data.get('Employee_activate'))
        empdict = emp.__dict__
        print(eid)
        print(empdict)
        msg = service.update_employee(eid, emp)
        if "joined" in msg:
            return json.dumps({"Success": msg})
        else:
            return json.dumps({"Error": msg})
    return json.dumps({'Error': 'Fields can not be empty'})


# @app.route('/employee/<int:eid>', methods=['PUT'])
# def update_employee(eid):
#     employee = Employee.query.filter_by(id=eid).first()
#     json_data = request.form
#     employee.name = json_data.get('Employee_name')
#     db.session.commit()
#     return json.dumps({"Success": "YES"})


@app.route('/employee/<int:eid>', methods=['DELETE'])
def delete_product(eid):
    msg = service.delete_employee(eid)
    if "deleted" in msg:
        return json.dumps({'Success': msg})
    else:
        return json.dumps({'Error': msg})
