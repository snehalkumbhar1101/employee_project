import os
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir

from dotenv import load_dotenv


# Load environment variables from a .env file if present
dotenv_path = abspath(join(dirname(__file__), pardir, '.env'))
load_dotenv(dotenv_path)

SERVICE_NAME = 'employee_project'
SERVICE_VERSION = '1.0.0'
os.environ['SERVICE_NAME'] = SERVICE_NAME

SENTRY = os.environ.get('SENTRY_DSN') or None

QA_ENVIRONMENT = 'qa'
DEV_ENVIRONMENT = 'dev'
PROD_ENVIRONMENT = 'prod'
TEST_ENVIRONMENT = 'test'

ENVIRONMENT = os.environ.get('Environment') or DEV_ENVIRONMENT
print(ENVIRONMENT)

ENVIRONMENTS = [QA_ENVIRONMENT, DEV_ENVIRONMENT, PROD_ENVIRONMENT, TEST_ENVIRONMENT]

if ENVIRONMENT not in ENVIRONMENTS:
    raise Exception('The environment used is not properly named')

# employee database credentials.
DB_CREDENTIALS = {
    'database': os.environ.get('MYSQL_DATABASE'),
    'host': os.environ.get('MYSQL_HOST'),
    'password': os.environ.get('MYSQL_PASSWORD'),
    'port': os.environ.get('MYSQL_PORT'),
    'user': os.environ.get('MYSQL_USER')
}

# Database connection configuration.

if ENVIRONMENT == DEV_ENVIRONMENT:
    DB_URL = (
        'mysql+pymysql://{user}:{password}@{host}/{db}?charset={charset}'
        .format(
            user=DB_CREDENTIALS.get('user'),
            password=DB_CREDENTIALS.get('password'),
            host=DB_CREDENTIALS.get('host'),
            db=DB_CREDENTIALS.get('database'),
            charset='utf8'))
