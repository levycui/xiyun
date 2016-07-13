#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""


import sys     #utf-8，兼容汉字



reload(sys)
sys.setdefaultencoding("utf-8")
from handlers.index import IndexHandler

from handlers.order import OrderHandler
from handlers.query import QueryHandler
from handlers.buyer import BuyerHandler
from handlers.goods import GoodsHandler
from handlers.agent import AgentHandler

from handlers.buy import NewHandler
from handlers.goods import GoodsAddHandler
from handlers.goodsupdate import GoodsUpdateHandler
from handlers.goodsupdate import GoodsUpdateHtmlHandler
from handlers.goodsupdate import GoodsUpdateChangeHandler
from handlers.goodslist import GoodsListHandler
from handlers.goods import GoodsAddNewHandler

from handlers.buyerAdd import BuyerAddHandler
from handlers.buyerAdd import BuyerAddNewHandler
from handlers.buyerlist import BuyerListHandler

url = [
    (r'/', IndexHandler),
    (r'/order.html', OrderHandler),
    (r'/query.html', QueryHandler),
    (r'/buyer.html', BuyerHandler),
    (r'/goods.html', GoodsHandler),
    (r'/goodsadd.html', GoodsAddHandler),
    (r'/goodslist.html', GoodsListHandler),
    (r'/goodsupdate.html', GoodsUpdateHtmlHandler),
    (r'/goodsUpdate', GoodsUpdateHandler),
    (r'/goodsUpdateChange', GoodsUpdateChangeHandler),
    (r'/buyeradd.html', BuyerAddHandler),
    (r'/buyerAdd', BuyerAddNewHandler),
    (r'/buyerlist.html', BuyerListHandler),
    # (r'/buyerUpdate', GoodsUpdateHandler),
    (r'/agent.html', AgentHandler),
    (r'/buy', NewHandler),
    (r'/goodsAdd', GoodsAddNewHandler),

]