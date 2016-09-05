#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import time
import methods.readdb as mrd

class OrderHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
        ordertime1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.render("order.html" ,ordertime=ordertime1)
