#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
import methods.insertdb as mrd

class GoodsHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("goods.html")

class GoodsAddHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("goodsadd.html")

class GoodsAddNewHandler(tornado.web.RequestHandler):
    def post(self):
        goodsnum = self.get_argument("goodsnum")
        goodsname = self.get_argument("goodsname")
        goodsprice = self.get_argument("goodsprice")
        goodssell = self.get_argument("goodssell")
        # if not weixinname:
        #     return None
        if not goodsnum.strip() or not goodsname.strip() or not goodsprice.strip() or not goodssell.strip() :
            self.write('this is error."货品编码\货品名称\进货价格\零售价格" 不能是空!')
            self.render("goodsadd.html")
        else:
            user_infos = mrd.goods_insert_table(table="goods",goodsnum=goodsnum,goodsname=goodsname,goodsprice=goodsprice,goodssell=goodssell)
            if not user_infos:
                self.write("数据添加成功！")
                self.render("goodsadd.html")
            else:
                self.write("this is error.")