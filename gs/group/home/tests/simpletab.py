# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from mock import patch, MagicMock
from unittest import TestCase
from gs.group.home.simpletab import (UserInfoTab, MemberOnlyTab, PublicTab, )


class UserInfoTabTest(TestCase):

    def create_tab(self):
        retval = UserInfoTab(group=MagicMock(), request=MagicMock(), view=MagicMock(),
                             manager=MagicMock())
        retval.userInfo = MagicMock()
        return retval

    @patch('gs.group.home.simpletab.user_member_of_group')
    def test_isMember(self, m_umog):
        'See if isMember returns True if the person is a member'
        m_umog.return_value = True
        t = self.create_tab()
        r = t.isMember

        self.assertTrue(r)

    @patch('gs.group.home.simpletab.user_member_of_group')
    def test_isMember_not(self, m_umog):
        'See if isMember returns False if the person is not a member'
        m_umog.return_value = False
        t = self.create_tab()
        r = t.isMember

        self.assertFalse(r)

    @patch('gs.group.home.simpletab.createObject')
    @patch('gs.group.home.simpletab.user_member_of_group')
    def test_canJoin_member(self, m_umog, m_cO):
        'Ensure members cannot join a group'
        m_umog.return_value = True
        ml = m_cO()
        ml.get_property.return_value = True

        t = self.create_tab()
        r = t.canJoin

        self.assertFalse(r)

    @patch('gs.group.home.simpletab.createObject')
    @patch('gs.group.home.simpletab.user_member_of_group')
    def test_canJoin_non_member(self, m_umog, m_cO):
        'Ensure non-members can join a group that is joinable'
        m_umog.return_value = False
        ml = m_cO()
        ml.get_property.return_value = True

        t = UserInfoTab(group=MagicMock(), request=MagicMock(), view=MagicMock(),
                        manager=MagicMock())
        t.userInfo = MagicMock()
        r = t.canJoin

        self.assertTrue(r)

    @patch('gs.group.home.simpletab.createObject')
    @patch('gs.group.home.simpletab.user_member_of_group')
    def test_canJoin_not_joinable(self, m_umog, m_cO):
        'Ensure non-members can only join a group that is joinable'
        m_umog.return_value = False
        ml = m_cO()
        ml.get_property.return_value = False

        t = self.create_tab()
        r = t.canJoin

        self.assertFalse(r)


class MemberOnlyTabTest(TestCase):

    def create_tab(self):
        retval = MemberOnlyTab(group=MagicMock(), request=MagicMock(), view=MagicMock(),
                               manager=MagicMock())
        retval.userInfo = MagicMock()
        return retval

    @patch('gs.group.home.simpletab.MemberOnlyTab.isMember')
    def test_show(self, m_iM):
        t = self.create_tab()
        t.isMember = True
        r = t.show

        self.assertTrue(r)

    @patch('gs.group.home.simpletab.MemberOnlyTab.isMember')
    def test_hide(self, m_iM):
        t = self.create_tab()
        t.isMember = False
        r = t.show

        self.assertFalse(r)


class PublicTabTest(TestCase):
    def create_tab(self):
        retval = PublicTab(group=MagicMock(), request=MagicMock(), view=MagicMock(),
                           manager=MagicMock())
        return retval

    @patch('gs.group.home.simpletab.PublicTab.viewTopics')
    def test_is_public(self, m_vT):
        'Ensure that the tab is shown if the topics are visible'
        t = self.create_tab()
        t.viewTopics = True
        r = t.show

        self.assertTrue(r)

    @patch('gs.group.home.simpletab.PublicTab.viewTopics')
    def test_is_hidden(self, m_vT):
        'Ensure that the tab is hidden if the topics are hidden'
        t = self.create_tab()
        t.viewTopics = False
        r = t.show

        self.assertFalse(r)
