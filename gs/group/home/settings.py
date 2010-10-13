# coding=utf-8
from zope.component import createObject
from Products.GSGroupMember.groupmembership import user_member_of_group
from Products.GSGroupMember.groupmembership import JoinableGroupsForSite
from simpletab import SimpleTab

class SettingsTab(SimpleTab):
    @property
    def isMember(self):
        userInfo = createObject('groupserver.LoggedInUser', self.context)
        return user_member_of_group(userInfo, self.groupInfo)

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

