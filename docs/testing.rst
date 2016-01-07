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
