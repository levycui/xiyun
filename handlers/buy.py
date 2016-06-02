#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.insertdb as mrd

class NewHandler(tornado.web.RequestHandler):
    def post(self):
        weixinname = self.get_argument("weixinname")
        username = self.get_argument("username")
        sex = self.get_argument("sex")
        age = self.get_argument("age")
        product1 = self.get_argument("product1")
        pnum1 = self.get_argument("pnum1")
        # product2 = self.get_argument("product2")
        # pnum2 = self.get_argument("pnum2")
        gift1 = self.get_argument("gift1")
        gnum1 = self.get_argument("gnum1")
        # gift2 = self.get_argument("gift2")
        # gnum2 = self.get_argument("gnum2")
        udate = self.get_argument("udate")
        # if not weixinname:
        #     return None
        if not weixinname.strip():
            self.write('this is error."weixinname" is null!')
        else:
            user_infos = mrd.insert_table(table="buy",weixinname=weixinname,username=username,sex=sex,age=age,product=product1,pnum=pnum1,gift=gift1,gnum=gnum1,udate=udate)
            if not user_infos:
                self.render("index.html")
            else:
                self.write("this is error.")
        # db = self.mrd.db
        # db.execute("insert into buy(weixinname,username,sex,age,product,pnum,gift,gnum,udate)" \
        #            "values('%s','%s','%d','%d','%s','%s','%s','%s','%s')", weixinname,username,sex,age,product1,pnum1,gift1,gnum1,udate)
        # self.redirect(".")
        # self.write("insert success.")
