# coding=utf-8
from zope.component import createObject
from Products.XWFCore.XWFUtils import getOption
from Products.GSGroupMember.groupmembership import user_division_admin_of_group
from simpletab import SimpleTab

class TopicsTab(SimpleTab):

    def only_group(self, *args):
        return True

    def only_author_link(self, *args):
        return False

    def only_group_link(self, *args):
        return False

    def get_search_url(self, **args):
        return ''

