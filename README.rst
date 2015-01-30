=================
``gs.group.home``
=================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The page for a GroupServer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-01-30
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This module mostly provides support for the `group page`_ for
GroupServer_ groups. Because the page is used by so many
different types of people for different things testing_ is
difficult.

Group page
==========

Most of the content for the *Group* page is provided by external
product.s The group page itself (``index.html`` in the group
context) is mostly made up of *five* viewlet managers, which
other products fill. Two managers provide spaces for the
information_ about the group. One provides space for information
and links concerning the administrators.  Finally, two more
viewlets provide the `metadata links`_ and scripts_ area that
support the other content providers. The arrangement of the five
viewlet managers is shown below::

  ┌Page────────────────────────────────────────────────────────────────────┐
  │┌Head──────────────────────────────────────────────────────────────────┐│
  ││gs.group.home.interfaces.IGroupHomepageMetadata                       ││
  │└──────────────────────────────────────────────────────────────────────┘│
  │┌Body──────────────────────────────────────────────────────────────────┐│
  ││┌───────────────────────────────┬────────────────────────────────────┐││
  │││Main information               │Secondary information               │││
  │││.interfaces.IGroupHomepageMain │.interfaces.IGroupHomepageSecondary │││
  │││                               │┌──────────────────────────────────┐│││
  │││                               ││Admin area                        ││││
  │││                               ││IGroupHomepageAdmin               ││││
  │││                               │└──────────────────────────────────┘│││
  ││└───────────────────────────────┴────────────────────────────────────┘││
  │└──────────────────────────────────────────────────────────────────────┘│
  │┌Scripts───────────────────────────────────────────────────────────────┐│
  ││gs.group.home.interfaces.IGroupHomepageScripts                        ││
  │└──────────────────────────────────────────────────────────────────────┘│
  └────────────────────────────────────────────────────────────────────────┘

Metadata links
--------------

The metadata for the Group page *mostly* consists of links to Web
feeds. These are organised by the viewlet manager
``gs.group.home.interfaces.IGroupHomepageMetadata`` — the
simplest of viewlet-managers: it just renders each viewlet (in
order) without any additional HTML:

.. code-block:: xml

  <browser:viewlet name="gs-group-messages-topics-link"
    manager="gs.group.home.interfaces.IGroupHomepageMetadata"
    template="browser/templates/link.pt"
    class="gs.group.home.simpletab.PublicTab"
    permission="zope2.View"
    weight="10"
    title="Topics Link" />

Information
-----------

There are two sets of information on the homepage: the `main
information`_ and the `secondary information`_.  Both are handled
by *viewlet managers*, with the blocks of information provided by
viewlets_.

:Note: To over-ride an existing tab, change the ``name`` of the
       viewlet to that of the viewlet you wish to overwrite.

Main information
~~~~~~~~~~~~~~~~

The main portion of the page (33 units wide) is taken up by the
*Main Information*.  The information tabs tells the user general
information about the group: what the group is for, and the main
activity in the group.

To add a tab to the info tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageMain`` as the manager:

.. code-block:: xml

  <browser:viewlet
    name="gs-group-messages-base" 
    manager="gs.group.home.interfaces.IGroupHomepageMain"
    class="gs.group.home.simpletab.PublicTab"
    template="browser/templates/main.pt"
    weight="50"
    permission="zope2.View"/>

Secondary information
~~~~~~~~~~~~~~~~~~~~~

Less important information about the group appears in the
*Secondary Information* area. It is normally formatted as a
narrow strip (15.5 units wide).

To add a tab to the task tabs create a *viewlet* that has
``gs.group.home.interfaces.IGroupHomepageSecondary`` as the
manager:

.. code-block:: xml

  <browser:viewlet
    name="gs-group-member-base-logged-in-member-info"
    manager="gs.group.home.interfaces.IGroupHomepageSecondary" 
    class=".memberinfo.LoggedInMemberInfo"
    template="browser/template/loggedinmemberinfo.pt"
    permission="zope2.View" 
    title="Membership Information"
    weight="10" />


Scripts
-------

Some of the content of the Group page may need JavaScript
support. The viewlets that supply the scripts are rendered by the
``gs.group.home.interfaces.IGroupHomepageScripts`` viewlet
manager.  Like the manager for the `metadata links`_, the scripts
manager renders each viewlet (in order) without any additional
HTML:

.. code-block:: xml

  <browser:viewlet 
    name="gs-group-messages-topics-tab-script"
    manager="gs.group.home.interfaces.IGroupHomepageScripts"
    template="browser/templates/topicstab-js.pt"
    class="gs.group.home.simpletab.PublicTab"
    permission="zope2.Public"
    weight="10"
    title="Topics" />

Testing
=======

To test that the homepage works the following user-and group
states must checked against the correct functioning of the
homepage. The correct functioning of the homepage is described in
the user-help. (For a secret group the anonymous and non-members
should not even see the group, so those tests are marked ``—``.)

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

Manager:
  A person with the ``manager`` role. Such people should be able
  to see and change everything, but not post unless he or she is
  a member.
  
Site Admin:
  A person with the ``DivisionAdmin`` role. A site administrator
  should be able to see the group, change all the permissions to
  do with the group, and alter the membership of the group. A
  site administrator can only post if he or she is a member of
  the group.

Group Admin:
  A person with the ``GroupAdmin`` role. A group administrator
  should be able to see the group, and change the membership of
  the group.
  
Posting Member:
  In announcement groups a posting member should be able to see
  the group, start new topics and post to existing topics.

Member:
  A member should be able to view the group and topics. In
  addition he or she can start a topic or post to a topic in a
  discussion group.

Non-Member:
  A non-member may or may not be able to view a group and topics,
  depending on the group privacy.
  
Anonymous:
  Someone who is not logged in (anonymous) may or may not be able
  to view a group and topics, depending on the group privacy.

A:
  Announcement group. Only some people can post to an
  announcement group. These people are known as *posting
  members*.

D:
  Discussion group. Every member of a discussion group should be
  able to post.

Todo
----

* Add site-admin-non-member and manager-non-member columns.
* Write down what to test.
* Create a list of the functional tests.
* Update the help so it matches the test.
* Automate the test.

Resources
=========

- Code repository: https://github.com/groupserver/gs.group.home
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _viewlets: http://docs.zope.org/zope.viewlet
