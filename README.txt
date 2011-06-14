Introduction
============

This module provides the group-homepage code for `GroupServer`_. It
mostly defines four viewlet managers, that other products fill. Two
managers provide `tabs`_. Two others provide the `admin links`_ and the
`us-bar links`_.

Tabs
----

There are two sets of tabs on the homepage: the `Info Tabs`_ and the
`Task Tabs`_. 

**Note** To over-ride an existing tab, change the ``name`` of the 
viewlet to that of the viewlet you wish to overwrite.

Info Tabs
~~~~~~~~~

The information tabs tells the user general information about the group:
the membership, statistics, and privacy for example. To add a tab to 
the info tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageInfo`` as the manager. The
``gs.group.base.viewlet.GroupViewlet`` provides a good base for a tab.

Task Tabs
~~~~~~~~~

The task tabs tells the user to carry out active tasks in the group:
the viewing topics, files, and changing settings for example. To add a 
tab to the task tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageTasks`` as the manager. The
``gs.group.base.viewlet.GroupViewlet`` provides a good base for a tab.

Admin Links
-----------

I need to document the admin links.

Us-Bar Links
------------

I need to document the us-bar links.

.. Resources

.. _GroupServer: http://groupserver.org

