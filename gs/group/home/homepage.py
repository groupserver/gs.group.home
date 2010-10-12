# coding=utf-8
from Products.Five import BrowserView
from zope.component import createObject

class GroupHomepage(BrowserView):
    def __init__(self, site, request):
        BrowserView.__init__(self, site, request)
        self.siteInfo = createObject('groupserver.SiteInfo', site)
        self.groupInfo = createObject('groupserver.GroupInfo', site)

