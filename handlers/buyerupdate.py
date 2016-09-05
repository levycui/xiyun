#!/usr/bin/env Python
# coding=utf-8
import time
import tornado.web
import methods.readdb as mrd
import methods.updatedb as updatemrd

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class BuyerUpdateHtmlHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("buyerupdate.html")



class BuyerUpdateHandler(tornado.web.RequestHandler):
    def post(self):
        buyerid = self.get_argument("buyerid")
        # goodsname = self.get_argument("goodsname")
        # goodsprice = self.get_argument("goodsprice")
        # goodssell = self.get_argument("goodssell")
        # if not weixinname:
        #     return None

        if not buyerid.strip():
            self.write('this is error."货品编码" 不能是空!')
        else:
            user_infos = mrd.select_buyerupdate(table="buyuser",column="*",condition="bid",value=buyerid)
            self.render("buyerupdate.html" ,lines=user_infos)
            # if not user_infos:
            #     # self.write("数据添加成功！")
            #     self.render("goodsupdate.html")
            # else:
            #     self.write("this is error.")

class BuyerUpdateChangeHandler(tornado.web.RequestHandler):
    def post(self):
        buyerid = self.get_argument("buyerid")
        weixinname = self.get_argument("weixinname")
        phonenum = self.get_argument("phonenum")
        sex = self.get_argument("sex")
        age = self.get_argument("age")
        username = self.get_argument("username")
        address1 = self.get_argument("address1")
        birsday = self.get_argument("birsday")
        address2 = self.get_argument("address2")
        if not buyerid:
            return None

        if not buyerid.strip() or not username.strip() or not phonenum.strip() :
            self.write('this is error."姓名\手机号" 不能是空!')
        else:
            user_infos = updatemrd.buyer_update_table(table="buyuser",weixinname=weixinname,phonenum=phonenum,sex=sex,age=age,username=username,address1=address1,birsday=birsday,address2=address2,buyerid=buyerid)
            if not user_infos:

                self.write("数据修改成功！")
                self.render("buyer.html", blogs=user_infos)

            else:
                self.write("this is error.")