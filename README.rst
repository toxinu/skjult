Skjult
==========

Description
-----------

Skjult help you to manage yours encfs containers.

Requirements
------------

- python 3 support
- encfs package (so linux)
- be in sudoers file
- modprobe fuse
- be in fuse group

Installation
------------

::

	pip install skjult

Examples
--------

Create container ::

	socketubs@socket-desktop:~$ skjult create mypr0n
	==> Create new secret
	[sudo] password for socketubs:
	Creating new encrypted volume.
	[encfs output...]

	New Encfs Password:
	Verify Encfs Password:

	socketubs@socket-desktop:~$ ls /media/
	mypr0n


List containers ::

	socketubs@socket-desktop:~$ skjult list
	==> All secrets
	mypr0n

Mount/umount container ::

	socketubs@socket-desktop:~$ skjult umount mypr0n
	socketubs@socket-desktop:~$ skjult mount mypr0n
	EncFS Password:

License
-------

License is `AGPL3`_. See `LICENSE`_.

.. _AGPL3: http://www.gnu.org/licenses/agpl.html
.. _LICENSE: https://git.socketubs.org/?p=skjult.git;a=blob_plain;f=LICENSE;hb=HEAD
