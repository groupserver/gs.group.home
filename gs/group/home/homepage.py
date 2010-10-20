# coding=utf-8
from Products.Five import BrowserView
from zope.component import createObject

class GroupHomepage(BrowserView):
    def __init__(self, group, request):
        BrowserView.__init__(self, group, request)
        self.siteInfo = createObject('groupserver.SiteInfo', group)
        self.groupInfo = createObject('groupserver.GroupInfo', group)

