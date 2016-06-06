#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""


import sys     #utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")
from handlers.index import IndexHandler
from handlers.buy import NewHandler
from handlers.order import OrderHandler
from handlers.query import QueryHandler
from handlers.buyer import BuyerHandler
from handlers.goods import GoodsHandler
from handlers.agent import AgentHandler


url = [
    (r'/', IndexHandler),
    (r'/order.html', OrderHandler),
    (r'/query.html', QueryHandler),
    (r'/buyer.html', BuyerHandler),
    (r'/goods.html', GoodsHandler),
    (r'/agent.html', AgentHandler),
    (r'/buy', NewHandler),
]