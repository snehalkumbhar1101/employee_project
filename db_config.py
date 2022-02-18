from flask_sqlalchemy import SQLAlchemy
from application import app
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:root@localhost/employee_db?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
