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
