#!/usr/bin/env Python
# coding=utf-8

from db import *

#购买新增
def insert_table(table, weixinname, username, roleid, product1, pnum1, product2, pnum2,product3, pnum3,product4, pnum4,product5, pnum5,product6, pnum6,product7, pnum7,product8, pnum8,product9, pnum9,product10, pnum10,product11, pnum11,product12, pnum12,gift1, gnum1,gift2, gnum2,gift3, gnum3,gift4, gnum4,gift5, gnum5,gift6, gnum6, udate):
    # sql = "insert " + column + " from " + table + " where " + condition + "='" + value + "'"
    sql = "insert into " + table + "(weixinname,username,roleid,product1,pnum1,product2,pnum2,product3,pnum3,product4,pnum4,product5,pnum5,product6,pnum6,product7,pnum7,product8,pnum8,product9,pnum9,product10,pnum10,product11,pnum11,product12,pnum12,gift1,gnum1,gift2,gnum2,gift3,gnum3,gift4,gnum4,gift5,gnum5,gift6,gnum6,udate) values('" + weixinname + "','" + username + "','" + roleid + "','" + product1 + "','" + pnum1 + "','" + product2 + "','" + pnum2 + "','" + product3 + "','" + pnum3 + "','" + product4 + "','" + pnum4 + "','" + product5 + "','" + pnum5 + "','" + product6 + "','" + pnum6 + "','" + product7 + "','" + pnum7 + "','" + product8 + "','" + pnum8 + "','" + product9 + "','" + pnum9 + "','" + product10 + "','" + pnum10 + "','" + product11 + "','" + pnum11 + "','" + product12 + "','" + pnum12 + "','" + gift1 + "','" + gnum1 + "','" + gift2 + "','" + gnum2 + "','" + gift3 + "','" + gnum3 + "','" + gift4 + "','" + gnum4 + "','" + gift5 + "','" + gnum5 + "','" + gift6 + "','" + gnum6 + "','" + udate + "')"
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