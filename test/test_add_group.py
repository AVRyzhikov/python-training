# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups import testdata

def test_add_group(app,db,json_groups):
    group=json_groups
    old_groups=db.get_group_list()
    #group=Group(name="xxx", header="yyyy", footer="zzzzz")
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max)==sorted(new_groups,key=Group.id_or_max)

#@pytest.mark.parametrize("group",testdata,ids=[repr(x) for x in testdata])
#def test_add_group(app,group):
#    pass
#    old_groups=app.group.get_group_list()
#    #group=Group(name="xxx", header="yyyy", footer="zzzzz")
#    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups,key=Group.id_or_max)==sorted(new_groups,key=Group.id_or_max)

#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



