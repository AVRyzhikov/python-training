from model.group import Group
import random

def test_delete_some_group(app,db,check_ui):
    if len(db.get_group_list()) ==0:
        app.group.create(Group(name="Test"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    #old_groups[index:index+1]=[]   # удаляем элементы с index до index+1 вырезка состоит из одного элемента с индексом ноль
    #old_groups[0:1] = []  # удаляем элементы с 0 до первого вырезка состоит из одного элемента с индексом ноль
    assert old_groups==new_groups
    if check_ui:
     #db_groups= sorted(new_groups,key=Group.id_or_max)
     #ui_groups= sorted(app.group.get_group_list(),key=Group.id_or_max)
     assert sorted(new_groups,key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)
     #assert db_groups == ui_groups