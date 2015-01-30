# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2010, 2013, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from gs.group.member.base.utils import user_member_of_group
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
