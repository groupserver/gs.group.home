# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.viewlet.interfaces import IViewletManager
from zope.schema import Text, ASCIILine
from zope.contentprovider.interfaces import IContentProvider
from Products.XWFCore.XWFUtils import abscompath
import gs.group.home


# Old:

class IGroupHomepageInfo(IViewletManager):
    '''A viewlet manager for the Info tabs on the group homepage'''


class IGroupHomepageTasks(IViewletManager):
    '''A viewlet manager for the Task tabs on the group homepage'''


class IGroupHomepageUsLinks(IViewletManager):

    '''A viewlet manager for the Us-Bar links on the group homepage'''


class IGroupHomepageUsBar(IContentProvider):
    groupId = ASCIILine(title=u'Group Identifier',
        description=u'The identifier for the group',
        required=True)

    pageTemplateFileName = Text(title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to '
                    u'render the status message.',
        required=False,
        default=abscompath(gs.group.home, "browser/templates/usbar.pt"))


# New:

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


class IGroupHomepageAdminLinks(IViewletManager):
    '''A viewlet manager for the administraton links on the group homepage'''
