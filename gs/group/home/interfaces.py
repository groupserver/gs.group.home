# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from zope.interface.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class IGroupHomepageMetadata(IViewletManager):
    '''A viewlet manager for the metadata on the group homepage'''


class IGroupHomepageMain(IViewletManager):
    '''A viewlet manager for the main information on the group homepage'''


class IGroupHomepageMessages(IViewletManager):
    '''A viewlet manager for the messages in the main section of the group
    homepage'''


class IGroupHomepageSecondary(IViewletManager):
    '''A viewlet manager for the secondary information on the group homepage'''


class IGroupHomepageScripts(IViewletManager):
    '''A viewlet manager for the scripts on the group homepage'''


class IGroupHomepageAdmin(IViewletManager):
    pass

# Legacy


class IChangeAbout(Interface):
    pass
