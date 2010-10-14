# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.viewlet.interfaces import IViewletManager
from zope.schema import Text, ASCIILine
from zope.contentprovider.interfaces import IContentProvider

class IGroupHomepageInfo(IViewletManager):
    '''A viewlet manager for the Info tabs on the group homepage'''

class IGroupHomepageTasks(IViewletManager):
    '''A viewlet manager for the Task tabs on the group homepage'''
    
class IGroupHomepageScripts(IViewletManager):
    '''A viewlet manager for the scripts on the group homepage'''
    
class IGroupHomepageUsBar(IContentProvider):
    groupId = ASCIILine(title=u'Group Identifier',
        description=u'The identifier for the group',
        required=True)

    pageTemplateFileName = Text(title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to '\
        u'render the status message.',
        required=False,
        default=u"browser/templates/usbar.pt")

