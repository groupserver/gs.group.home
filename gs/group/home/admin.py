# coding=utf-8
from zope.component import createObject
from Products.XWFCore.XWFUtils import getOption
from Products.GSGroupMember.groupmembership import user_division_admin_of_group, user_group_admin_of_group
from simpletab import UserInfoTab

class AdminTab(UserInfoTab):
    def __init__(self, group, request, view, manager):
        UserInfoTab.__init__(self, group, request, view, manager)
        self.__mailingListInfo = None
        
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
        if self.__mailingListInfo == None:
            self.__mailingListInfo = createObject('groupserver.MailingListInfo', 
                                               self.context)
        return self.__mailingListInfo

    @property
    def isAnnouncement(self):
        template = self.groupInfo.get_property('group_template')
        return template == 'announcement'
        
    @property
    def isSiteAdmin(self):
        return user_division_admin_of_group(self.userInfo, self.groupInfo)

    @property
    def isGroupAdmin(self):
        return user_group_admin_of_group(self.userInfo, self.groupInfo)

    @property
    def canSetPostingLimit(self):
        return getOption(self.context, 'admin_can_set_posting_limit', True)

