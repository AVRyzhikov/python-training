__author__='alexandr'
from sys import maxsize
class Contact:
    def __init__(self,firstname=None,lastname=None,id=None,
                 all_phones_from_home_page=None,
                 homephone=None,mobilephone=None,workphone=None):
        # соответсвующие поля не проинициализированы
        # указывать при вызове конструктора их необязательно в этих полях особое спец. значение None
        self.firstname=firstname
        self.lastname=lastname
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.homephone=homephone
        self.mobilephone = mobilephone
        self.workphone = workphone


    def __repr__(self):
        return "%s:%s %s" %(self.id, self.firstname,self.lastname )

    def __eq__(self,other):
        return (self.id==None or other.id==None or self.id==other.id) \
               and self.firstname==other.firstname and self.lastname==other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
