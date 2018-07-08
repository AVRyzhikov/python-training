from pytest_bdd import scenario
from .group_steps import *  # импортируем все шаги

@scenario('groups.feature','Add new group')   # 1 - название файла со сценариями и 2 название сценария
def test_add_new_group():
    pass # реализация уже сделана в сценарии ишагах

@scenario('groups.feature','Delete a group')   # 1 - название файла со сценариями и 2 название сценария
def test_delete_group():
    pass # реализация уже сделана в сценарии ишагах