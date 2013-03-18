# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from Products.XWFCore.XWFUtils import getOption
from gs.group.member.base.utils import user_division_admin_of_group, \
    user_group_admin_of_group
from simpletab import UserInfoTab


class AdminTab(UserInfoTab):
    def __init__(self, group, request, view, manager):
        super(AdminTab, self).__init__(group, request, view, manager)

    @Lazy
    def memberCount(self):
        acl_users = self.context.acl_users
        assert acl_users, 'Aquisition bites'
        userGroupId = '%s_member' % self.groupInfo.id
        userGroup = acl_users.getGroupById(userGroupId)
        retval = len(userGroup.getUsers())
        return retval

    @Lazy
    def mailingListInfo(self):
        retval = createObject('groupserver.MailingListInfo', self.context)
        return retval

    @property
    def isAnnouncement(self):
        template = self.groupInfo.get_property('group_template')  # FIXME
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
