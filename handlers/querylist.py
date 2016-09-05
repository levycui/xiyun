#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from methods.db import *

class QueryListHandler(tornado.web.RequestHandler):

    def showAllBlog(self):
        cur.execute('select uid,weixinname,username,sex,age,product,pnum,gift,gnum,udate from buy')
        tmp = cur.fetchall()
        return tmp[::-1]

    def get(self):
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()
        self.render('querylist.html', cookieName=name, blogs=blogs)


