#!/bin/bash

SQL="
CREATE USER ${MYSQL_USERNAME} IDENTIFIED BY '${MYSQL_PASSWORD}';
CREATE DATABASE ${DATABASE_NAME} DEFAULT CHARACTER SET utf8;

GRANT ALL ON *.* to ${MYSQL_USERNAME}@localhost IDENTIFIED BY '${MYSQL_PASSWORD}';
GRANT ALL ON *.* to ${MYSQL_USERNAME}@\"%\" IDENTIFIED BY '${MYSQL_PASSWORD}';
"

echo "$SQL" | mysql -uroot -p${MYSQL_ROOT_PASSWORD}