#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class BuyerHandler(tornado.web.RequestHandler):
    def get(self):
        #usernames = mrd.select_columns(table="user",column="username")
        #one_user = usernames[0][0]
        #self.render("index.html", user=one_user)
        self.render("buyer.html")
