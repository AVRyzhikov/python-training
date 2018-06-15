__author__='alexandr'
from sys import maxsize
class Group:
    def __init__(self,name=None,header=None,footer=None,id=None):
        # соответсвующие поля не проинициализированы
        # указывать при вызове конструктора их необязательно в этих полях особое спец. значение None
        self.name=name
        self.header=header
        self.footer=footer
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self,other):
        return (self.id==None or other.id==None or self.id==other.id) and self.name==other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
