# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.contentprovider.interfaces import IContentProvider
from zope.interface.interface import Interface
from zope.schema import Text, ASCIILine
from zope.viewlet.interfaces import IViewletManager
from Products.XWFCore.XWFUtils import abscompath
import gs.group.home


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
