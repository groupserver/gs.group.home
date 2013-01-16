# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from Products.GSGroupMember.groupMembersInfo import GSGroupMembersInfo
from gs.group.base import GroupViewlet
from gs.group.privacy.visibility import GroupVisibility


class GroupStats(GroupViewlet):

    def __init__(self, group, request, view, manager):
        super(GroupStats, self).__init__(group, request, view, manager)

    @Lazy
    def membersInfo(self):
        retval = GSGroupMembersInfo(self.groupInfo.groupObj)
        return retval

    @Lazy
    def visibility(self):
        retval = GroupVisibility(self.groupInfo)
        return retval
