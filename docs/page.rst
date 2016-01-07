Group page
==========

Most of the content for the *Group* page is provided by external
products. The group page itself (``index.html`` in the group
context) is mostly made up of *five* viewlet managers, which
other products fill. Two managers provide spaces for the
information_ about the group. One provides space for information
and links concerning the administrators. Finally, two more
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

.. _viewlets: http://docs.zope.org/zope.viewlet
