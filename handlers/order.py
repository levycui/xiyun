#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import time
from methods.db import *

import methods.insertdb as mrd

class OrderHandler(tornado.web.RequestHandler):
    def showAllBlog(self):
        cur.execute('select gnum,ggoodsname from goods')
        tmp = cur.fetchall()
        return tmp[::-1]

    def get(self):
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()
        self.render('order.html', cookieName=name, blogs=blogs)

    # def get(self):
    #     #usernames = mrd.select_columns(table="user",column="username")
    #     #one_user = usernames[0][0]
    #     #self.render("index.html", user=one_user)
    #     # ordertime1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     # self.render("order.html" ,ordertime=ordertime1)
    #     self.render("order.html")

class OrderNewHandler(tornado.web.RequestHandler):
    def post(self):
        weixinname = self.get_argument("weixinname")
        username = self.get_argument("username")
        roleid = self.get_argument("roleid")
        # age = self.get_argument("age")
        product1 = self.get_argument("product1")
        pnum1 = self.get_argument("pnum1")
        product2 = self.get_argument("product2")
        pnum2 = self.get_argument("pnum2")
        product3 = self.get_argument("product3")
        pnum3 = self.get_argument("pnum3")
        product4 = self.get_argument("product4")
        pnum4 = self.get_argument("pnum4")
        product5 = self.get_argument("product5")
        pnum5 = self.get_argument("pnum5")
        product6 = self.get_argument("product6")
        pnum6 = self.get_argument("pnum6")
        product7 = self.get_argument("product7")
        pnum7 = self.get_argument("pnum7")
        product8 = self.get_argument("product8")
        pnum8 = self.get_argument("pnum8")
        product9 = self.get_argument("product9")
        pnum9 = self.get_argument("pnum9")
        product10 = self.get_argument("product10")
        pnum10 = self.get_argument("pnum10")
        product11 = self.get_argument("product11")
        pnum11 = self.get_argument("pnum11")
        product12 = self.get_argument("product12")
        pnum12 = self.get_argument("pnum12")

        gift1 = self.get_argument("gift1")
        gnum1 = self.get_argument("gnum1")
        gift2 = self.get_argument("gift2")
        gnum2 = self.get_argument("gnum2")
        gift3 = self.get_argument("gift3")
        gnum3 = self.get_argument("gnum3")
        gift4 = self.get_argument("gift4")
        gnum4 = self.get_argument("gnum4")
        gift5 = self.get_argument("gift5")
        gnum5 = self.get_argument("gnum5")
        gift6 = self.get_argument("gift6")
        gnum6 = self.get_argument("gnum6")

        udate = self.get_argument("udate")
        # if not weixinname:
        #     return None
        if not weixinname.strip():
            self.write('this is error.微信号不能为空!')
            self.render("order.html")

        else:
            user_infos = mrd.insert_table(table="buy",weixinname=weixinname,username=username,roleid=roleid,product1=product1,pnum1=pnum1,product2=product2,pnum2=pnum2,product3=product3,pnum3=pnum3,product4=product4,pnum4=pnum4,product5=product5,pnum5=pnum5,product6=product6,pnum6=pnum6,product7=product7,pnum7=pnum7,product8=product8,pnum8=pnum8,product9=product9,pnum9=pnum9,product10=product10,pnum10=pnum10,product11=product11,pnum11=pnum11,product12=product12,pnum12=pnum12,gift1=gift1,gnum1=gnum1,gift2=gift2,gnum2=gnum2,gift3=gift3,gnum3=gnum3,gift4=gift4,gnum4=gnum4,gift5=gift5,gnum5=gnum5,gift6=gift6,gnum6=gnum6,udate=udate)
            if not user_infos:
                self.write("添加成功！")
                self.render("index.html")
            else:
                self.write("this is error.")
        # db = self.mrd.db
        # db.execute("insert into buy(weixinname,username,sex,age,product,pnum,gift,gnum,udate)" \
        #            "values('%s','%s','%d','%d','%s','%s','%s','%s','%s')", weixinname,username,sex,age,product1,pnum1,gift1,gnum1,udate)
        # self.redirect(".")
        # self.write("insert success.")
