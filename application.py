from raven.contrib import flask
import raven.contrib

from employee_details import app
from employee_details import config
# from employee_details import handlers
if config.SENTRY:
    app.app.config['SENTRY_DSN'] = config.SENTRY
    raven.contrib.flask.Sentry(app.app)

app = app.app
