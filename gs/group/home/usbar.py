# coding=utf-8
from zope.component import createObject
from zope.contentprovider.interfaces import UpdateNotCalled
from zope.app.pagetemplate import ViewPageTemplateFile
from Products.GSGroupMember.groupmembership import user_member_of_group
from gs.group.base.contentprovider import GroupContentProvider
from queries import UsQuery

class UsBar(GroupContentProvider):
    def __init__(self, context, request, view):
        GroupContentProvider.__init__(self, context, request, view)
        self.__updated = False
        self.__isMember = self.__userInfo = None

    # TODO: Move self.userInfo and self.isMember to a base
    #   gs.group.member.base.GroupMemberContentProvider class
    @property
    def userInfo(self):
        if self.__userInfo == None:
            self.__userInfo = createObject('groupserver.LoggedInUser', 
                                            self.context)
        return self.__userInfo
        
    @property
    def isMember(self):
        if self.__isMember == None:
            self.__isMember = user_member_of_group(self.userInfo, 
                                                    self.context)
        return self.__isMember
        
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

