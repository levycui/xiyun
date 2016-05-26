#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="user",column="*",condition="username",value=username)

        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.render("user.html", users = user_infos)
                #self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")
