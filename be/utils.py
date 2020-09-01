import os

CONFIG = {}

CONFIG['YB_SERVER_HOST']= os.getenv('YB_SERVER_HOST', 'localhost')
CONFIG['YB_SERVER_PORT']= int(os.getenv('YB_SERVER_PORT', 7777))
CONFIG['YB_DB_HOST']    = os.getenv('YB_DB_HOST', 'localhost')
CONFIG['YB_DB_PORT']    = int(os.getenv('YB_DB_PORT', 6666))
CONFIG['YB_DB_USER']    = os.getenv('YB_DB_USER', 'root')
CONFIG['YB_DB_PW']      = os.getenv('YB_DB_PW', 'test1234')
CONFIG['YB_DB_DB']      = os.getenv('YB_DB_DB', 'yellowbus')
