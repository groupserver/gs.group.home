# coding=utf-8
from zope.component import createObject
from AccessControl import getSecurityManager

class SimpleTab(object):
    @property
    def siteInfo(self):
        return createObject('groupserver.SiteInfo', self.context)
        
    @property
    def groupInfo(self):
        return createObject('groupserver.GroupInfo', self.context)

    @property
    def viewTopics(self):
        # --=mpj17=-- If the user can view the messages the he or she
        #   can view almost all of the sub-pages. This is *mostly* used
        #   to tell the difference between a Public and Private group.
        #   (Non-members cannot even see a Secret group, so it is not
        #   much of an issue.)
        #
        # TODO: Figure out I could do this better.
        msgs = self.context.messages
        user = getSecurityManager().getUser()
        retval = bool(user.has_permission('View', msgs))
        return retval

