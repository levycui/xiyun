#!/usr/bin/env Python
# coding=utf-8
import time
import tornado.web
from methods.db import *
import methods.readdb as mrd
import methods.updatedb as updatemrd


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class QueryUpdateHtmlHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
        self.render("queryupdate.html")



class QueryUpdateHandler(tornado.web.RequestHandler):
    def showAllBlog(self):
        cur.execute('select gnum,ggoodsname from goods')
        tmp = cur.fetchall()
        return tmp[::-1]

    def post(self):
        orderid = self.get_argument("orderid")
        # goodsname = self.get_argument("goodsname")
        # goodsprice = self.get_argument("goodsprice")
        # goodssell = self.get_argument("goodssell")
        # if not weixinname:
        #     return None
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()





        if not orderid.strip():
            self.write('this is error."订单编码" 不能是空!')
        else:

            user_infos = mrd.select_queryupdate(table="buy",column="*",condition="uid",value=orderid)
            # for b in blogs:
            #     for bp in user_infos:
            #         if b[0] == bp[4]:
            #             bvalue = b[1]
            bvalue =[]
            for n in 4,12,13,14,15,16,17,18,19,20,21,22:
                for bp in user_infos:
                    for b in blogs:
                        if bp[n] == b[0] :
                            bvalue.append(b[1])
            if len(bvalue) != 12:
                num = 12 - len(bvalue)
                for c in range(num):
                    bvalue.append("无")


            self.render("queryupdate.html" ,cookieName=name, blogs=blogs,lines=user_infos,bvalue=bvalue)
            # if not user_infos:
            #     # self.write("数据添加成功！")
            #     self.render("goodsupdate.html")
            # else:
            #     self.write("this is error.")

class QueryUpdateChangeHandler(tornado.web.RequestHandler):
    def post(self):
        orderid = self.get_argument("orderid")
        weixinname = self.get_argument("weixinname")
        username = self.get_argument("username")
        sex = self.get_argument("sex")
        age = self.get_argument("age")
        product1 = self.get_argument("product1")
        pnum1 = self.get_argument("pnum1")
        gift1 = self.get_argument("gift1")
        gnum1 = self.get_argument("gnum1")
        udate = self.get_argument("udate")
        if not orderid:
            return None

        if not orderid.strip() or not weixinname.strip() or not username.strip() :
            self.write('this is error."微信号\姓名" 不能是空!')
        else:
            user_infos = updatemrd.query_update_table(table="buy",orderid=orderid,weixinname=weixinname,username=username,sex=sex,age=age,product=product1,pnum=pnum1,gift=gift1,gnum=gnum1,udate=udate)
            if not user_infos:

                self.write("数据修改成功！")
                self.render("index.html", blogs=user_infos)

            else:
                self.write("this is error.")