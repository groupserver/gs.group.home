# coding=utf-8
from queries import UsQuery

class UsBar(object):
    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.__updated = False

        self.context = context
        self.request = request

    def update(self):
        self.postingMembers = []
        uq = UsQuery(self.context.zsqlalchemy)
        self.postingMembers = uq.posting_authors('siteId', 'groupId')

    def render(self):
        return u'<p>The Us Bar</p>'

