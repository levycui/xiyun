#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from methods.db import *

class QueryListHandler(tornado.web.RequestHandler):

    def showAllBlog(self):
        cur.execute('select uid,weixinname,username,roleid,product1,pnum1,product2,pnum2,product3,pnum3,product4,pnum4,product5,pnum5,product6,pnum6,product7,pnum7,product8,pnum8,product9,pnum9,product10,pnum10,product11,pnum11,product12,pnum12,gift1,gnum1,gift2,gnum2,gift3,gnum3,gift4,gnum4,gift5,gnum5,gift6,gnum6,udate from buy')
        tmp = cur.fetchall()
        return tmp[::-1]

    def get(self):
        name = self.get_cookie('hackerName')
        blogs = self.showAllBlog()
        self.render('querylist.html', cookieName=name, blogs=blogs)


