Introduction
============

This module provides the group-homepage code for `GroupServer`_. It
mostly defines four viewlet managers, that other products fill. Two
managers provide `tabs`_. Two others provide the `admin links`_ and the
`us-bar links`_.

Tabs
----

There are two sets of tabs on the homepage: the `Info Tabs`_ and the
`Task Tabs`_.  Both sets of tabs are handled by *viewlet managers*,
with the tabs appearing as `viewlets`_. The viewlets have to provide a
``<div>`` element, which will be styled by `jQuery.UI`_.

**Note** To over-ride an existing tab, change the ``name`` of the 
viewlet to that of the viewlet you wish to overwrite.

Info Tabs
~~~~~~~~~

The information tabs tells the user general information about the group:
the membership, statistics, and privacy for example. 

To add a tab to the info tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageInfo`` as the manager. The
``gs.group.base.viewlet.GroupViewlet`` provides a good base for a tab.

Task Tabs
~~~~~~~~~

The task tabs tells the user to carry out active tasks in the group:
the viewing topics, files, and changing settings for example.

To add a tab to the task tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageTasks`` as the manager. The
``gs.group.base.viewlet.GroupViewlet`` provides a good base for a tab.

Admin Links
-----------

The Admin tab contains links to many of the administration functions
within a group. The tab is a viewlet, sitting instide the `task
tabs`_. However, the tab is also a *viewlet manager*: it contains
viewlets that link to the administration pages.

To add a link to the admin links create a viewlet that has
``gs.group.home.interfaces.IGroupHomepageAdminLinks`` as the manager. The
``gs.group.member.base.viewlet.GroupAdminViewlet`` provides a good base
for the viewlet code. The viewlet itself should provide a list-item
element (``<li>``) to appear in the tab.

Us-Bar Links
------------

I need to document the us-bar links.

.. Resources

.. _GroupServer: http://groupserver.org
.. _viewlets: http://jqueryui.com/demos/tabs/
.. _jQuery.UI: http://jqueryui.com/demos/tabs/

