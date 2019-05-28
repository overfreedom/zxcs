#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

MYSQL_DB = 'zxcs'
MYSQL_USER = 'root'
MYSQL_PASS = 'sa'
MYSQL_HOST ='localhost'

connection = pymysql.connect(host = MYSQL_HOST, user=MYSQL_USER,
                            password =MYSQL_PASS, db =MYSQL_DB)

if __name__ == "__main__":
    sql = 'select now()'    
    print(connection.cursor().execute(sql))
    pass