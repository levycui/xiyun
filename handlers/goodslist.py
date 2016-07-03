#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from methods.db import *

class GoodsListHandler(tornado.web.RequestHandler):

    def showAllBlog(self):
        cur.execute('select gnum, ggoodsname, ggoodsprice, ggoodssell from goods')
        tmp = cur.fetchall()
        return tmp[::-1]

    def get(self):
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()
        self.render('goodslist.html', cookieName=name, blogs=blogs)


