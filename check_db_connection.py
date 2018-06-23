#import mysql.connector

#connection=mysql.connector.connect(host="127.0.0.1",
#                                   database="addressbook",
#                                   user="root",password="") #локальная машина
#try:
#    cursor=connection.cursor()
#    cursor.execute("select * from group_list")
#    for row  in cursor.fetchall():
#        print(row)
#finally:
#    connection.close()
#from fixture.db import DbFixture
#db=DbFixture(host="127.0.0.1",
#                                   name="addressbook",
#                                   user="root",password="") #локальная машина
#try:
#3    contacts=db.get_contact_list()
#    for contact in contacts:
#        print(contact)
#    print(len(contacts))

#finally:
#    db.destroy()

from fixture.orm import  ORMFixture
from model.group import Group

db=ORMFixture(host="127.0.0.1",
                                   name="addressbook",
                                   user="root",password="") #локальная машина
#try:
#     l=db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))

#try:
#     l=db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))


#finally:
#     pass #db.destroy() # ORM автоматически закрывает соединение с БД, меняем на заглушку

try:
     l=db.get_contacts_in_group(Group(id='155'))
     for item in l:
         print(item)
     print(len(l))


finally:
     pass #db.destroy() # ORM автоматически закрывает соединение с БД, меняем на заглушку