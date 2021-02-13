# transportSharing
Transport sharing implementation in Python w/ Sanic

## Quick Start

[./db/init.sql](./db/init.sql)을 통해서 MySQL init 후,

```Shell
# Install required libs

$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt

# Set up environment variables or use the default values.

$ export YB_SERVER_HOST=""  # default localhost     서버가 돌아가는 HOST
$ export YB_SERVER_PORT=""  # default 7777          서버가 돌아가는 PORT
$ export YB_DB_HOST=""      # default localhost     MySQL DB가 돌아가는 HOST
$ export YB_DB_PORT=""      # default 3306          MySQL DB가 돌아가는 PORT
$ export YB_DB_USER=""      # default root          MySQL DB USER
$ export YB_DB_PW=""        # default test1234      MySQL DB PASSWORD
$ export YB_DB_DB=""        # default yellowbus     MySQL DB에서 사용할 Database

$ python3 main.py 
```

---

## API Guide

* 노선 정보 생성 API

> POST Request의 JSON body에 대응하는 노선을 생성합니다. 노선의 이름은 Unique 합니다. 정류장은 최대 10개까지 있습니다.

http://[YB_SERVER_HOST]:[YB_SERVER_PORT]/api/v1/create_route

Method: ['POST']

Request Body:
```JSON
{
    "name": "노선 이름",
    "courses": [
        {"name": "정류장 이름", "order": 1},
        ...
        {"name": "정류장 이름", "order": N <= 10}
    ]
}
```
Response:
```JSON
{
    "result": "success"
}
```

![alt text][create1]
![alt text][create2]
![alt text][create3]
![alt text][create4]

</br></br>

---

* 노선 정보 조회 API

> 모든 노선의 ID와 이름을 출력합니다.

http://[YB_SERVER_HOST]:[YB_SERVER_PORT]/api/v1/route

Method: ['GET']

Request Body:
```JSON
None
```
Response:
```JSON
{
    "courses": [
        {"id": id, "name": "노선 이름"},
        ...
    ]
}
```

![alt text][allroute1]

</br></br>

---

* 노선 상세보기 API

> URI의 <route_id>에 해당하는 노선의 ID와 이름, 코스를 출력합니다.

http://[YB_SERVER_HOST]:[YB_SERVER_PORT]/api/v1/route/<route_id>

Method: ['GET']

Request Body:
```JSON
None
```
Response:
```JSON
{
    "id": route_id,
    "name": "노선 이름"
    "course": [
        {"name": "정류장 이름", "order": 1},
        ...
        {"name": "정류장 이름", "order": N <= 10},
    ]
}
```

![alt text][oneroute1]

</br></br>

---

* 노선 정보 수정 API

> URI의 <route_id>에 해당하는 노선의 이름을 Request JSON Body["name"]으로 수정합니다.

http://[YB_SERVER_HOST]:[YB_SERVER_PORT]/api/v1/route/<route_id>


Method: ['PUT']

Request Body:
```JSON
{
    "name": "새로운 노선 이름",
}
```
Response:
```JSON
{
    "result": "success"
}
```

![alt text][modify1]
![alt text][modify2]

</br></br>

---

* 노선 정보 삭제 API

> URI의 <route_id>에 해당하는 노선을 삭제합니다.

http://[YB_SERVER_HOST]:[YB_SERVER_PORT]/api/v1/route/<route_id>

Method: ['DELETE']

Request Body:
```JSON
None
```
Response:
```JSON
{
    "result": "success"
}
```

![alt text][delete1]
![alt text][delete2]

</br></br>

---
---

## SQL Guide

[./db/init.sql](./db/init.sql)을 통해서 MySQL init

---
</br></br>

* route

```SQL
CREATE TABLE route (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_name` VARCHAR(32) NOT NULL UNIQUE,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;
```
</br></br>

---
</br></br>

* route_order

```SQL
CREATE TABLE route_order (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_id` INT UNSIGNED NOT NULL,
    `course_id` INT UNSIGNED NOT NULL,
    `order` SMALLINT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`course_id`) REFERENCES course(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`route_id`) REFERENCES route(`id`) ON DELETE CASCADE
);
```

</br></br>

---
</br></br>

* course

```SQL
CREATE TABLE course (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `course_name` VARCHAR(32) NOT NULL UNIQUE,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;
```
</br></br>

---
---

[create1]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/create1.png "create1"
[create2]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/create2.png "create2"
[create3]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/create3.png "create3"
[create4]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/create4.png "create4"
[delete1]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/delete1.png "delete1"
[delete2]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/delete2.png "delete2"
[modify1]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/modify1.png "modify1"
[modify2]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/modify2.png "modify2"
[allroute1]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/allroute1.png "allroute1"
[oneroute1]: https://github.com/woodchuckchoi/yellowBus/blob/master/images/oneroute1.png "oneroute1"
