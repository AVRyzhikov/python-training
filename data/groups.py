# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

testdata=[ Group(name="name 1", header="header 1", footer="footer 1"),
           Group(name="name 2", header="header 2", footer="footer 2")
         ]


#def random_string(prefix,maxlen):
#    symbols=string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata=[
#             Group(name=name, header=header, footer=footer)
#             for name in ["",random_string("name ",10)]
#             for header in["",random_string("header ",20)]
#             for footer in["",random_string("footer ",20)]
#
#         ]
