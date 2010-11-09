# coding=utf-8
from Products.GSGroup.interfaces import IGSMailingListInfo
from Products.GSGroupMember.usercanpost import GSGroupMemberPostingInfo
from simpletab import UserInfoTab

class TopicsTab(UserInfoTab):
    def __init__(self, group, request, view, manager):
        UserInfoTab.__init__(self, group, request, view, manager)
        self.__canPost = None
        self.__email = None
            
    @property
    def canPost(self):
        if self.__canPost == None:
            canPost = GSGroupMemberPostingInfo(self.groupInfo.groupObj, 
                                                self.userInfo)
            self.__canPost = canPost.canPost
        return self.__canPost
        
    @property
    def email(self):
        if self.__email == None:
            l = IGSMailingListInfo(self.groupInfo.groupObj)
            self.__email = l.get_property('mailto')
        return self.__email

