#!/usr/bin/env Python
# coding=utf-8

from db import *


def insert_table(table, weixinname):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(weixinname) values('" + weixinname + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines
