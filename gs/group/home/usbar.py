# coding=utf-8
from zope.component import createObject
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.app.pagetemplate import ViewPageTemplateFile
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from settings import SettingsTab
from queries import UsQuery

class UsBar(SettingsTab):
    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.__updated = False

        self.context = context
        self.request = request
        self.__updated = False
        
    def update(self):
        self.__updated = True

        self.postingMembers = []
        if self.viewTopics:
            # If you cannot see the topics you should not see who posted
            uq = UsQuery(self.context.zsqlalchemy)
            ml = uq.posting_authors(self.siteInfo.id, self.groupInfo.id)
            ctx = self.context
            self.postingMembers = \
                [createObject('groupserver.UserFromId',ctx, uid) for uid in ml]

    def render(self):
        if not self.__updated:
            raise UpdateNotCalled

        pageTemplate = ViewPageTemplateFile(self.pageTemplateFileName)
        return pageTemplate(self)

