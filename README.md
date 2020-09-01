# yellowBus
Yellow Bus implementation in Python w/ Sanic

## API Guide

## SQL Guide

### route

```SQL
CREATE TABLE route (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_name` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;
```

### route_order

```SQL
CREATE TABLE route_order (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_id` INT UNSIGNED NOT NULL,
    `stop_id` INT UNSIGNED NOT NULL,
    `order` SMALLINT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`stop_id`) REFERENCES stop(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`route_id`) REFERENCES route(`id`) ON DELETE CASCADE
);
```

### stop

```SQL
CREATE TABLE stop (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `stop_name` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;
```
