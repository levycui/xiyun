#!/usr/bin/env Python
# coding=utf-8

from db import *


def goods_update_table(table, goodsname, goodsprice, goodssell, goodsnum):
    # sql = "update " + table + "(gnum, ggoodsname, ggoodsprice, ggoodssell) values('" + goodsnum + "','" + goodsname + "','" + goodsprice + "','" + goodssell + "')"
    sql = "update " + table + " set ggoodsname = '" + goodsname + "', ggoodsprice = '" + goodsprice + "', ggoodssell = '" + goodssell + "' where gnum='" + goodsnum +"'"

    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines

def buyer_update_table(table, weixinname, phonenum, sex, age,username,address1,birsday,address2,buyerid):
    # sql = "update " + table + "(gnum, ggoodsname, ggoodsprice, ggoodssell) values('" + goodsnum + "','" + goodsname + "','" + goodsprice + "','" + goodssell + "')"
    sql = "update " + table + " set bweixinname = '" + weixinname + "', busername = '" + username + "', bsex = '" + sex + "' ,bage = '" + age + "', bbirthday = '" + birsday + "', bphone = '" + phonenum + "', baddress1 = '" + address1 + "', baddress2 = '" + address2 + "' where bid='" + buyerid +"'"

    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines

def query_update_table(table,weixinname,username,sex,age,product,pnum,gift,gnum,udate,orderid):
    # sql = "update " + table + "(gnum, ggoodsname, ggoodsprice, ggoodssell) values('" + goodsnum + "','" + goodsname + "','" + goodsprice + "','" + goodssell + "')"
    sql = "update " + table + " set weixinname = '" + weixinname + "', username = '" + username + "', sex = '" + sex + "' ,age = '" + age + "', product = '" + product + "', pnum = '" + pnum + "', gift = '" + gift + "', gnum = '" + gnum + "', udate = '" + udate + "' where uid='" + orderid +"'"

    cur.execute(sql)
    lines = cur.fetchall()
    conn.commit()
    return lines
