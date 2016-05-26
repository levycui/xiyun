#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class NewHandler(tornado.web.RequestHandler):
    def post(self):
        weixinname = self.get_argument("weixinname")
        username = self.get_argument("username")
        sex = self.get_argument("sex")
        age = self.get_argument("age")
        product1 = self.get_argument("product1")
        pnum1 = self.get_argument("pnum1")
        product2 = self.get_argument("product2")
        pnum2 = self.get_argument("pnum2")
        gift1 = self.get_argument("gift1")
        gnum1 = self.get_argument("gnum1")
        gift3 = self.get_argument("gift2")
        gnum2 = self.get_argument("gnum2")
        pdate = self.get_argument("pdate")
        if not weixinname:
            return None
        db = self.mrd.db
        db.execute("insert into buy(weixinname,username,sex,age,product,pnum,gift,gnum,udate)" \
                   "values('%s','%s','%d','%d','%s','%s','%s','%s','%s')", weixinname,username,sex,age,product1,pnum1,gift1,gnum1,pdate)
        self.redirect(".")
        self.write("insert success.")
