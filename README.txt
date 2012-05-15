Introduction
============

This module provides the group-homepage code for `GroupServer`_. It
mostly defines *six* viewlet managers, that other products fill. Two
managers provide `tabs`_. Two others provide the `administration links`_
and the `us-bar links`_. Finally, two more provide the `metadata links`_
and `scripts`_ area that support the other content providers.

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

Administration Links
--------------------

The **Admin** tab contains links to many of the administration functions
within a group. The tab is a viewlet, sitting inside the `task
tabs`_. However, the tab is also a *viewlet manager*: it contains
viewlets that link to the administration pages.

To add a link to the administration links create a viewlet that has
``gs.group.home.interfaces.IGroupHomepageAdminLinks`` as the manager. The
class ``gs.group.member.base.viewlet.GroupAdminViewlet`` provides a
good base class for the viewlet. The viewlet itself should provide a
list-item element (``<li>``) to appear in the tab.

To further complicate things, the ``gs.group.properties.base`` module
defines a viewlet that contains *another* viewlet manager. This allows
the links related to the properties of the group to be clustered
together.

The viewlets that provide the administration should be shown to the
correct *type* of administrator. In GroupServer there are three types
of administrator.

1. A **group administrator** only changes the membership of people.
2. A **site administrator** can change the membership of people, change
   the properties of a group, and start a new group.
3. A **manager** is the GroupServer of a super-user. In the context of
   a group a manager has the same powers as a site administrator.

Us-Bar Links
------------

The us-bar contains some links to do with changing membership:

* Signing up,
* Joining,
* Requesting membership, and
* Leaving

The links themselves are provided by the respective modules. All the
homepage does is provide the viewlet manager that displays the links.

To add a link to the us-bar create a viewlet that has
``gs.group.home.interfaces.IGroupHomepageUsLinks`` as the manager. The
class ``gs.group.member.base.viewlet.MemberViewlet`` provides a good
base class for the viewlet. The viewlet itself should provide a list-item
element (``<li>``) to appear in the us-bar links.

Metadata Links
--------------

The metadata for the Group page *mostly* consists of links to Web 
feeds. These are organised by the viewlet manager
``gs.group.home.interfaces.IGroupHomepageMetadata`` — the simplest of 
viewlet-managers: it just renders each viewlet (in order) without any
additional HTML.

Scripts
-------

Some of the content of the Group page may need JavaScript support. The
viewlets that supply the scripts are rendered by the 
``gs.group.home.interfaces.IGroupHomepageScripts`` viewlet manager.
Like the manager for the `metadata links`_, the scripts manager renders
each viewlet (in order) without any additional HTML.

Testing
=======

To test that the homepage works the following user-and group states must
checked against the correct functioning of the homepage. The correct
functioning of the homepage is described in the user-help. (For a secret
group the anonymous and non-members should not even see the group,
so those tests are marked ``—``.)

+---------+---------+-------+-------+---------+--------+-------+-------+
|         | Manager | Site  | Group | Posting | Normal | Non-  | Anon  |
|         |         | Admin | Admin | Member  | Member | Member|       |
+---------+----+----+---+---+---+---+----+----+---+----+---+---+---+---+
|         | A  | D  | A | D | A | D | A  | D  | A | D  | A | D | A | D |
+=========+====+====+===+===+===+===+====+====+===+====+===+===+===+===+
| Public  | ✓  | ✓  | ✓ | ✓ | ✓ | ✓ | ✓  | —  | ✓ | ✓  | ✓ | ✓ | ✓ | ✓ |
+---------+----+----+---+---+---+---+----+----+---+----+---+---+---+---+
| Private | ✓  | ✓  | ✓ | ✓ | ✓ | ✓ | ✓  | —  | ✓ | ✓  | ✓ | ✓ | ✓ | ✓ |
+---------+----+----+---+---+---+---+----+----+---+----+---+---+---+---+
| Secret  | ✓  | ✓  | ✓ | ✓ | ✓ | ✓ | ✓  | —  | ✓ | ✓  | — | — | — | — |
+---------+----+----+---+---+---+---+----+----+---+----+---+---+---+---+

Manager
  A person with the ``manager`` role. Such people should be able to see
  and change everything, but not post unless he or she is a member.
  
Site Admin
  A person with the ``DivisionAdmin`` role. A site administrator should
  be able to see the group, change all the permissions to do with the
  group, and alter the membership of the group. A site administrator
  can only post if he or she is a member of the group.

Group Admin
  A person with the ``GroupAdmin`` role. A group administrator should
  be able to see the group, and change the membership of the group.
  
Posting Member
  In announcement groups a posting member should be able to see the
  group, start new topics and post to existing topics.

Member
  A member should be able to view the group and topics. In addition he
  or she can start a topic or post to a topic in a discussion group.

Non-Member
  A non-member may or may not be able to view a group and topics,
  depending on the group privacy.
  
Anonymous
  Someone who is not logged in (anonymous) may or may not be able to 
  view a group and topics, depending on the group privacy.  

A
  Announcement group. Only some people can post to an announcement
  group. These people are known as *posting members*.

D
  Discussion group. Every member of a discussion group should be able
  to post.

Todo
-----

* Add site-admin-non-member and manager-non-member columns.
* Write down what to test.
* Create a list of the functional tests.
* Update the help so it matches the test.
* Automate the test.

.. Resources

.. _GroupServer: http://groupserver.org
.. _viewlets: http://jqueryui.com/demos/tabs/
.. _jQuery.UI: http://jqueryui.com/demos/tabs/

