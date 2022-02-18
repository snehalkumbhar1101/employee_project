import os
# from employee_details import models
# from employee_details import handlers
# from employee_details.connectors.mysql import db_engine
from db_config import db
from application import app
from employee_details import handlers

if __name__ == '__main__':
    db.create_all()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)


