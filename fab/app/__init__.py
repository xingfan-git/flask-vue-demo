import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from flask_cors import CORS

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__,
            static_folder="../../frontend/dist/static",
            template_folder="../../frontend/dist")
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from app import views