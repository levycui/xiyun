#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.readdb as mrd
import methods.updatedb as updatemrd

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class GoodsUpdateHtmlHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
         self.render("goodsupdate.html")



class GoodsUpdateHandler(tornado.web.RequestHandler):
    def post(self):
        goodsnum = self.get_argument("goodsnum")
        # goodsname = self.get_argument("goodsname")
        # goodsprice = self.get_argument("goodsprice")
        # goodssell = self.get_argument("goodssell")
        # if not weixinname:
        #     return None

        if not goodsnum.strip():
            self.write('this is error."货品编码" 不能是空!')
        else:
            user_infos = mrd.select_goodsupdate(table="goods",column="*",condition="gnum",value=goodsnum)
            self.render("goodsupdate.html" ,lines=user_infos)
            # if not user_infos:
            #     # self.write("数据添加成功！")
            #     self.render("goodsupdate.html")
            # else:
            #     self.write("this is error.")

class GoodsUpdateChangeHandler(tornado.web.RequestHandler):
    def post(self):
        goodsnum = self.get_argument("goodsnum")
        goodsname = self.get_argument("goodsname")
        goodsprice = self.get_argument("goodsprice")
        goodssell = self.get_argument("goodssell")
        if not goodsnum:
            return None

        if not goodsnum.strip() or not goodsname.strip() or not goodsprice.strip() or not goodssell.strip() :
            self.write('this is error."货品编码\货品名称\进货价格\零售价格" 不能是空!')
        else:
            user_infos = updatemrd.goods_update_table(table="goods",goodsname=goodsname,goodsprice=goodsprice,goodssell=goodssell,goodsnum=goodsnum)
            if not user_infos:
                self.write("数据修改成功！")
                self.render("goodslist.html", blogs=user_infos)
            else:
                self.write("this is error.")