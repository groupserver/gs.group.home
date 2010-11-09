# coding=utf-8
from zope.component import createObject
from gs.group.base.contentprovider import GroupContentProvider
from Products.GSGroupMember.interfaces import IGSPostingUser
from Products.GSGroupMember.groupmembership import user_member_of_group

class TopicsTab(GroupContentProvider):
    def __init__(self, group, request, view, manager):
        GroupContentProvider.__init__(self, group, request, view)
        self.manager = manager
        self.__canPost = None
            
    @property
    def canPost(self):
        if self.__canPost == None:
            ui = createObject('groupserver.LoggedInUser', self.context)
            canPost = IGSPostingUser(ui)
            self.__canPost = canPost.canPost
        return self.__canPost
        
    @property
    def isMember(self):
        u = createObject('groupserver.LoggedInUser', self.context)
        return user_member_of_group(u, self.context)

