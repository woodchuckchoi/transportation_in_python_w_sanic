import os
import time
import uuid

def load_config(app):
    app.config.SERVERHOST   = os.getenv('YB_SERVER_HOST', '0.0.0.0')
    app.config.SERVERPORT   = int(os.getenv('YB_SERVER_PORT', 7777))
    app.config.DBHOST       = os.getenv('YB_DB_HOST', 'localhost')
    app.config.DBPORT       = int(os.getenv('YB_DB_PORT', 3306))
    app.config.DBUSER       = os.getenv('YB_DB_USER', 'root')
    app.config.DBPW         = os.getenv('YB_DB_PW', 'test1234')
    app.config.DBNAME       = os.getenv('YB_DB_DB', 'yellowbus')

def log_request(request):
    print('''{:5} | {:<15} | {:<100} | {:1024}\n'''.format(time.strftime('%M:%S'), request.ip, str(request.headers), str(request.body)))