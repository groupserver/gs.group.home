# coding=utf-8
from zope.component import createObject
from gs.group.base.contentprovider import GroupContentProvider
from Products.GSGroup.interfaces import IGSMailingListInfo
from Products.GSGroupMember.usercanpost import GSGroupMemberPostingInfo
from Products.GSGroupMember.groupmembership import user_member_of_group

class TopicsTab(GroupContentProvider):
    def __init__(self, group, request, view, manager):
        GroupContentProvider.__init__(self, group, request, view)
        self.manager = manager
        self.__canPost = None
        self.__email = None
            
    @property
    def canPost(self):
        if self.__canPost == None:
            ui = createObject('groupserver.LoggedInUser', self.context)
            canPost = GSGroupMemberPostingInfo(self.groupInfo.groupObj, ui)
            self.__canPost = canPost.canPost
        return self.__canPost
        
    @property
    def isMember(self):
        print 'Deprecated'
        u = createObject('groupserver.LoggedInUser', self.context)
        return user_member_of_group(u, self.context)

    @property
    def email(self):
        if self.__email == None:
            l = IGSMailingListInfo(self.groupInfo.groupObj)
            self.__email = l.get_property('mailto')
        return self.__email

