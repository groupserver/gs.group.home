# coding=utf-8
from zope.component import createObject

class SimpleTab(object):
    @property
    def siteInfo(self):
        return createObject('groupserver.SiteInfo', self.context)
        
    @property
    def groupInfo(self):
        return createObject('groupserver.GroupInfo', self.context)

