#!/usr/bin/env Python
# coding=utf-8

from db import *

#购买新增
def insert_table(table, weixinname, username, sex, age, product, pnum, gift, gnum, udate):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(weixinname,username,sex,age,product,pnum,gift,gnum,udate) values('" + weixinname + "','" + username + "','" + sex + "','" + age + "','" + product + "','" + pnum + "','" + gift + "','" + gnum + "','" + udate + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines

#货品新增
def goods_insert_table(table, goodsnum, goodsname, goodsprice, goodssell):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(gnum, ggoodsname, ggoodsprice, ggoodssell) values('" + goodsnum + "','" + goodsname + "','" + goodsprice + "','" + goodssell + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines

#买家新增
def buyer_insert_table(table,weixinname,username,sex,age,birsday,phonenum,address1,address2,bdate):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(bweixinname, busername, bsex, bage, bbirthday,bphone,baddress1,baddress2,bdate) values('" + weixinname + "','" + username + "','" + sex + "','" + age + "','" + birsday + "','" + phonenum + "','" + address1 + "','" + address2 + "','" + bdate + "')"
    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines