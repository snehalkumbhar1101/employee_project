from flask import Flask
from employee_details import config


app = Flask(config.SERVICE_NAME)


def test_client():
    return None