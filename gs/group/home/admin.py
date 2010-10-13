# coding=utf-8
from zope.component import createObject
from Products.XWFCore.XWFUtils import getOption
from Products.GSGroupMember.groupmembership import user_division_admin_of_group
from simpletab import SimpleTab

class AdminTab(SimpleTab):
    @property
    def memberCount(self):
        acl_users = self.context.acl_users
        assert acl_users, 'Aquisition bites'
        userGroupId = '%s_member' % self.groupInfo.id
        userGroup = acl_users.getGroupById(userGroupId)
        retval = len(userGroup.getUsers())
        return retval

    @property
    def mailingListInfo(self):
        mailingListInfo = createObject('groupserver.MailingListInfo', 
                                        self.context)
        return mailingListInfo

    @property
    def isAnnouncement(self):
        template = self.groupInfo.get_property('group_template')
        return template == 'announcement'
        
    @property
    def isSiteAdmin(self):
        userInfo = createObject('groupserver.LoggedInUser', self.context)
        return user_division_admin_of_group(userInfo, self.groupInfo)

    @property
    def canSetPostingLimit(self):
        return getOption(self.context, 'admin_can_set_posting_limit', True)

