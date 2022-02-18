from db_config import db
from datetime import datetime


class Employee(db.Model):
    __tablename__ = "Employee_Info"
    id = db.Column('emp_id', db.Integer(), primary_key=True)
    name = db.Column('emp_name', db.String(length=30))
    email_id=db.Column('emp_email',db.String(length=50))
    phone_number=db.Column('emp_phone_number',db.CHAR(10))
    position=db.Column('emp_position',db.String(length=30))
    salary = db.Column('emp_salary', db.Float())
    joined_date = db.Column('emp_joined', db.DateTime(),
                            default=datetime.now,onupdate=datetime.now)
    active = db.Column('active', db.String(10), default="Y")


def fetch_employee(eid):
    return None