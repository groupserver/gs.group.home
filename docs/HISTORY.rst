Changelog
=========

4.0.3 (2016-01-08)
------------------

* Moving the *Admin* area towards the top, so it is unmoved by
  the dynamic elements (such as the *Recently active* list and
  the *Recent files* list).
* Moving the documentation to Read the Docs
* Adding unit tests
  
4.0.2 (2014-09-17)
------------------

* Name the reStructuredText files as such
* Move to GitHub_ as the primary code repository

.. _GitHub: https://github.com/groupserver/gs.group.home

4.0.1 (2014-08-29)
------------------

* Minor page tidy
* Metadata update

4.0.0 (2014-05-28)
------------------

* Update for the new GroupServer user interface

  + Reconfigure into two columns: primary and secondary
  + Added a breadcrumb list
  + Dropping the old *Login* link
  + Cleaning up the working of the *Admin* list
  
* Updated the documentation
* Removing old interfaces
* Following the split of `gs.group.member.base`_

3.3.0 (2012-06-22)
------------------

* Update the SQLAlchemy_

.. _SQLAlchemy: http://www.sqlalchemy.org/

3.2.0 (2012-05-25)
------------------

* Moving the *About* tab to `gs.group.about`_

.. _gs.group.about: https://github.com/groupserver/gs.group.about

3.1.0 (2012-05-15)
------------------

* Moving the *Files* tab to `gs.group.messages.files`_
* Adjusting the weights of the *Admin* tab, and the *Settings* tab
* Using the marker interface in `gs.group.base`_
* Adding a viewlet manager for the metadata

.. _gs.group.messages.files: https://github.com/groupserver/gs.group.messages.files

3.0.0 (2012-05-02)
------------------

* Moved the *Topics* tab to `gs.group.messages.topics`_

.. _gs.group.messages.topics: https://github.com/groupserver/gs.group.messages.topics


2.2.1 (2011-07-13)
------------------

* Removing the word *Home* from the homepage title (only sites
  have homepages, groups only have a *group page*)

2.2.0 (2011-07-01)
------------------

* Showing the correct links at the bottom of the *Topics* tab
* Moved the *Change properties* links to their own viewlet
* Updated documentation
* Fix for the *Can post* code

2.1.0 (2011-06-06)
------------------

* Simplifying the code for the *Topic* tab
* Following the *Can post* code to `gs.group.member.canpost`_

.. _gs.group.member.canpost: https://github.com/groupserver/gs.group.member.canpost

2.0.0 (2011-05-23)
------------------

* Adding a *Login* link to the *Us* bar
* Moving the *Change* links
* Refactor of the code for the viewlets into `gs.group.base`_ and
  `gs.group.member.base`_

.. _gs.group.base: https://github.com/groupserver/gs.group.base
.. _gs.group.member.base: https://github.com/groupserver/gs.group.member.base

1.4.3 (2011-03-04)
------------------

* Adding a ``isGroupAdmin`` check

1.4.2 (2011-02-23)
------------------

* Fixing a typing mistake

1.4.1 (2011-01-28)
------------------

* Updating the ``jQuery.UI`` version

1.4.0 (2011-01-12)
-------------------

* Adding a JavaScript *sharebox*

1.3.0 (2010-12-17)
------------------

* Highlighting the posting instructions
* Adding help

1.2.1 (2010-12-09)
------------------

* Using the new form-message content provider

1.2.0 (2010-12-03)
------------------

* Linking to the correct *Change email settings* page
* Linking to the correct *Members* page
* Making the text in the *About* tab optional
* CSS fixes

1.1.0 (2010-11-26)
------------------

* Update the *About* page
* Link to the *Change group properties* page
* Minor XML changes

1.0.0 (2010-11-10)
------------------

Initial version. Group homepages prior to this lacked tabs, and
were produced by templates (``Templates/output``) in the Zope
Management Interface (ZMI).

..  LocalWords:  sharebox Changelog CSS ZMI viewlets github groupserver GitHub
..  LocalWords:  reStructuredText
