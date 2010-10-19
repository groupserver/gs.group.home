# coding=utf-8
from zope.component import createObject
from Products.GSGroupMember.groupmembership import JoinableGroupsForSite
from simpletab import SimpleTab

class UserInfoTab(SimpleTab):
    @property
    def isAnon(self):
        userInfo = createObject('groupserver.LoggedInUser', self.context)
        return userInfo.anonymous

    @property
    def canJoin(self):
        mailingListInfo = createObject('groupserver.MailingListInfo', 
                                        self.context)
        retval = not(self.isMember) and mailingListInfo.get_property('subscribe')
        return retval

class SettingsTab(UserInfoTab):
    @property
    def show(self):
        return self.isMember

class FilesTab(UserInfoTab):
    @property
    def show(self):
        return self.viewTopics

