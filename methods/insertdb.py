#!/usr/bin/env Python
# coding=utf-8

from db import *


def insert_table(table, weixinname, username, sex, age, product, pnum, gift, gnum, udate):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(weixinname,username,sex,age,product,pnum,gift,gnum,udate) values('" + weixinname + "','" + username + "','" + sex + "','" + age + "','" + product + "','" + pnum + "','" + gift + "','" + gnum + "','" + udate + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines

def goods_insert_table(table, goodsnum, goodsname, goodsprice, goodssell):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(gnum, ggoodsname, ggoodsprice, ggoodssell) values('" + goodsnum + "','" + goodsname + "','" + goodsprice + "','" + goodssell + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines