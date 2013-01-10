# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from Products.GSGroupMember.groupmembership import user_member_of_group
from gs.group.base import GroupViewlet


class SimpleTab(GroupViewlet):
    def __init__(self, group, request, view, manager):
        super(SimpleTab, self).__init__(group, request, view, manager)
        # FIXME: Deprecate


class UserInfoTab(GroupViewlet):
    def __init__(self, group, request, view, manager):
        super(UserInfoTab, self).__init__(group, request, view, manager)

    @Lazy
    def isMember(self):
        retval = user_member_of_group(self.userInfo, self.context)
        return retval

    @Lazy
    def canJoin(self):
        mailingListInfo = createObject('groupserver.MailingListInfo',
                                        self.context)
        retval = not(self.isMember) and \
                    mailingListInfo.get_property('subscribe')
        return retval


class MemberOnlyTab(UserInfoTab):
    @Lazy
    def show(self):
        return self.isMember


class PublicTab(UserInfoTab):
    @Lazy
    def show(self):
        return self.viewTopics
