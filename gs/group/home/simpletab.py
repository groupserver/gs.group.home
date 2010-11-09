# coding=utf-8
from zope.component import createObject
from AccessControl import getSecurityManager
from gs.group.base.contentprovider import GroupContentProvider
from Products.GSGroupMember.groupmembership import user_member_of_group

class SimpleTab(GroupContentProvider):
    def __init__(self, group, request, view, manager):
        GroupContentProvider.__init__(self, group, request, view)
        self.manager = manager

class UserInfoTab(SimpleTab):
    def __init__(self, group, request, view, manager):
        SimpleTab.__init__(self, group, request, view, manager)
        self.manager = manager
        self.__userInfo = None
        self.__isMember = None
    
    @property
    def userInfo(self):
        if self.__userInfo == None:
            self.__userInfo = createObject('groupserver.LoggedInUser', 
                                            self.context)
        return self.__userInfo
        
    @property
    def isMember(self):
        if self.__isMember == None:
            self.__isMember = user_member_of_group(self.userInfo, 
                                                    self.context)
        return self.__isMember

    @property
    def canJoin(self):
        mailingListInfo = createObject('groupserver.MailingListInfo', 
                                        self.context)
        retval = not(self.isMember) and mailingListInfo.get_property('subscribe')
        return retval
  
class MemberOnlyTab(UserInfoTab):
    @property
    def show(self):
        return self.isMember

class PublicTab(UserInfoTab):
    @property
    def show(self):
        return self.viewTopics

