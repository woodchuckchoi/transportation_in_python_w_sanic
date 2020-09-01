CREATE DATABASE yellowbus;
ALTER DATABASE [DB명] DEFAULT CHARACTER SET utf8;

USE yellowbus;

CREATE TABLE stop (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `stop_name` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;

CREATE TABLE route (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_name` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
)
DEFAULT CHARACTER SET = utf8;

CREATE TABLE route_order (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `route_id` INT UNSIGNED NOT NULL,
    `stop_id` INT UNSIGNED NOT NULL,
    `order` SMALLINT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`stop_id`) REFERENCES stop(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`route_id`) REFERENCES route(`id`) ON DELETE CASCADE
);