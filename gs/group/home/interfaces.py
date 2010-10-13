# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.interface import Attribute
from zope.viewlet.interfaces import IViewletManager
from zope.schema import List, Text, Bool, Choice
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

class IGroupHomepageInfo(IViewletManager):
    '''A viewlet manager for the Info tabs on the group homepage'''

class IGroupHomepageTasks(IViewletManager):
    '''A viewlet manager for the Task tabs on the group homepage'''
    
class IGroupHomepageScripts(IViewletManager):
    '''A viewlet manager for the scripts on the group homepage'''
