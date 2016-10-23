#!/usr/bin/env Python
# coding=utf-8

import time
import tornado.web
import methods.readdb as mrd
import methods.insertdb as mrd

class BuyerHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("buyer.html")

class BuyerAddHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("buyeradd.html")

class BuyerAddNewHandler(tornado.web.RequestHandler):
    def post(self):
        weixinname = self.get_argument("weixinname")
        phonenum = self.get_argument("phonenum")
        sex = self.get_argument("sex")
        age = self.get_argument("age")
        username = self.get_argument("username")
        address1 = self.get_argument("address1")
        birsday = self.get_argument("birsday")
        address2 = self.get_argument("address2")
        # if not weixinname:
        #     return None
        if not weixinname.strip() or not phonenum.strip() :
            self.write('this is error."微信号\手机号" 不能是空!')
            self.render("buyeradd.html")
        else:
            bdate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            user_infos = mrd.buyer_insert_table(table="buyuser",weixinname=weixinname,phonenum=phonenum,sex=sex,age=age,username=username,address1=address1,birsday=birsday,address2=address2,bdate=bdate)
            if not user_infos:
                self.write("数据添加成功！")
                self.render("buyeradd.html")
            else:
                self.write("this is error.")