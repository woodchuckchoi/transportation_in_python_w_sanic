from sanic import Sanic
from sanic.response import json

import aiomysql

from .utils import load_config, log_request

app = Sanic(__name__)
load_config(app)


# Listener

@app.listener('before_server_start')
async def db_init(app, loop):
    app.pool = await aiomysql.create_pool(host=app.config.DBHOST, port=app.config.DBPORT, \
        user=app.config.DBUSER, password=app.config.DBPW, db=app.config.DBNAME, loop=loop)

@app.listener('after_server_stop')
async def db_end(app, loop):
    app.pool.close()
    await app.pool.wait_closed()


# Middleware

@app.middleware('request')
async def log(request):
    log_request(request)

@app.middleware('response')
async def add_headers(request, response):
    # headers to add
    pass


# Router

# 노선 정보 생성 API - Done
@app.route('api/v1/create_route', methods=['POST'])
async def create_route(request):
    try:
        route_name  = request.json['name']
        courses     = list(map(lambda x: [x['name'], x['order']], request.json['courses']))
        course_names= list(map(lambda x: x[0], courses))
        # check if order is valid, other errors will be caught during SQL insertion
        assert list(map(lambda x: x['order'], request.json['courses'])) == list(range(1, len(courses)+1)) and len(courses) <= 10, 'Order is not valid.'
    
    except AssertionError as err:
        return json({'result': str(err)}, status=#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)

    async with app.pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await cur.execute("INSERT INTO route(route_name) VALUES ('{}');".format(route_name))

                for course_name in course_names:
                    try:
                        await cur.execute("INSERT INTO course(course_name) VALUES ('{}');".format(course_name))
                    except:
                        pass

                insert_query = "INSERT INTO route_order(`route_id`, `course_id`, `order`) VALUES \
                ((SELECT id FROM route WHERE route_name='{}'),".format(route_name)
                insert_query += "(SELECT id FROM course WHERE course_name='{}'), {});"
                
                for course in courses:
                    await cur.execute(insert_query.format(course[0], course[1]))
            
                await conn.commit()
            
            except Exception as err:
                await conn.rollback()
                return json({'result': str(err)})

    return json({'result': 'success'})


# 노선 정보 조회 API - DONE
@app.route('api/v1/route', methods=['GET'])
async def create_route(request):
    async with app.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT id, route_name FROM route ORDER BY id;")
                ret = await cur.fetchall()
                
                try:
                    assert len(ret) > 0, "No route"

                except AssertionError as err:
                    return json({'courses': []})
                    
                ret = list(map(lambda x: {'id': x[0], 'name': x[1]}, ret))
    return json({'courses': ret})


# 노선 정보 수정 API - DONE
@app.route('api/v1/route/<route_id>', methods=['PUT'])
async def create_route(request, route_id):
    try:
        route_id = int(route_id)
        new_name = request.json['name']
        async with app.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    ret = await cur.execute("UPDATE route SET route_name='{}' WHERE id={};".format(new_name, route_id))
                    await conn.commit()
        
    except Exception as err:
        return json({'result': str(err)})

    return json({'result': 'success'})


# 노선 상세보기 API - DONE
@app.route('api/v1/route/<route_id>', methods=['GET'])
async def create_route(request, route_id):
    try:
        route_id = int(route_id)
        async with app.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT route.route_name, course.course_name, route_order.order \
                        FROM route INNER JOIN route_order ON route.id=route_order.route_id \
                        INNER JOIN course ON route_order.course_id=course.id \
                        WHERE route.id={} ORDER BY route_order.order;".format(route_id))
                    ret = await cur.fetchall()
                    assert len(ret) > 0, 'No match'
                    ret = {
                        'id'    : route_id,
                        'name'  : ret[0][0],
                        'course': [
                            {
                                'name': course[1],
                                'order': course[2]
                            }
                            for course in ret
                        ]
                    }
    except AssertionError as err:
        return json({'result': str(err)})
    
    except Exception as err:
        return json({'result': str(err)})

    return json(ret)

# 노선 정보 삭제 API - DONE
@app.route('api/v1/route/<route_id>', methods=['DELETE'])
async def create_route(request, route_id):
    try:
        route_id = int(route_id)
        async with app.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("DELETE FROM route WHERE id={};".format(route_id))
                    await conn.commit()
    
    except Exception as err:
        return json({'result': str(err)})

    return json({'result': 'success'})