__author__='alexandr'
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:

    db=Database()

    class ORMGroup(db.Entity): # наследуем от db.Entity
        _table_='group_list'
        id=PrimaryKey(int,column='group_id')
        name=Optional(str,column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # lambda функция возвращаюшая класс contact
        contacts=Set(lambda: ORMFixture.ORMContact,table ="address_in_groups", column="id", reverse="groups",lazy=True)

    class ORMContact(db.Entity): # наследуем от db.Entity
        _table_='addressbook'
        id=PrimaryKey(int,column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        #deprecated = Optional(datetime, column='deprecated')
        deprecated = Optional(str, column='deprecated')
        groups=Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id",reverse="contacts",lazy=True)

        #groups = Set(ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts',lazy=True)


    def __init__(self,host,name,user,password): # потому что конструктор
        self.db.bind('mysql',host=host, database=name,   # тип базы данных и набор папаметров
                                   user=user,password=password)         #,conv=decoders
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self,groups):
        def convert(group):  # конвертация одной группы
            return Group(id=str(group.id),name=group.name,header=group.header,footer=group.footer)
        return list(map(convert,groups))


    def get_group_list1(self):
        # каждый блок кода, в котором происходит взаимодействие с БД, должен быть особым образом помечен
        # необходимо указать, что этот блок кода выполняется в рамках сессии
        with db_session:
            return list(select(g for g in  ORMFixture.ORMGroup)) # делаем выборку из оюъектов данног класса
        # результатом выполлнеия является запрос, а нам нужен список объектов, поэтому преобразовываем в список


    @db_session
    def get_group_list(self):
        # каждый блок кода, в котором происходит взаимодействие с БД, должен быть особым образом помечен
        # необходимо указать, что этот блок кода выполняется в рамках сессии
        return self.convert_groups_to_model(select(g for g in  ORMFixture.ORMGroup))

    def convert_contacts_to_model(self,contacts):
        def convert(contact):  # конвертация одного контакта
            return Contact(id=str(contact.id),firstname=contact.firstname,lastname=contact.lastname)

        return list(map(convert,contacts))

    @db_session
    def get_contact_list(self):
        #contacts = select(c for c in ORMFixture.ORMContact if c.deprecated is None)
        # каждый блок кода, в котором происходит взаимодействие с БД, должен быть особым образом помечен
        # необходимо указать, что этот блок кода выполняется в рамках сессии
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None)) #if c.deprecated is None

    #0000-00-00 00:00:00
    @db_session
    def get_contacts_in_group(self,group):
        orm_group=list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return self.convert_groups_to_model(orm_group.contacts)
