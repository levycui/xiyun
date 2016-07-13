#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from methods.db import *

class BuyerListHandler(tornado.web.RequestHandler):

    def showAllBlog(self):
        cur.execute('select bid, bweixinname, busername, bsex, bage, bbirthday,bphone,baddress1,baddress2 from buyuser')
        tmp = cur.fetchall()
        return tmp[::-1]

    def get(self):
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()
        self.render('buyerlist.html', cookieName=name, blogs=blogs)


