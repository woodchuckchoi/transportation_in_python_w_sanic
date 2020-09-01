from sanic import Sanic
from aiomysql

from .utils import CONFIG

app = Sanic(__name__)

@app.listener('before_server_start')
async def db_init(app, loop):
    db_host, db_port = get_db_conn_config()
    app.pool = await aiomysql.create_pool(host=CONFIG['YB_DB_HOST'], port=CONFIG['YB_DB_PORT'], \
        user=CONFIG['YB_DB_USER'], password=CONFIG['YB_DB_PW'], db=CONFIG['YB_DB_DB'], loop=loop)

@app.listener('after_server_stop')
async def db_end(app, loop):
    app.pool.close()
    await pool.wait_closed()