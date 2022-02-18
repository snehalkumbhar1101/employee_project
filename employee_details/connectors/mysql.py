"""MySQL Connector.
Manages iteraction with MySQL Database.
"""

from sqlalchemy import create_engine
from employee_details import config


db_engine = create_engine(config.DB_URL)
print(db_engine)
print("database connected")
