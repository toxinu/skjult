Skjult
==========

Description
-----------

Skjult help you to manage yours encfs containers.

Requirements
------------

  You need encfs package (so linux)
  You need to be in sudoers file
  You need to modprobe fuse
  You need to be in fuse group

Examples
--------

Create container ::

	socketubs@socket-desktop:~$ skjult create mypr0n
	==> Create new secret
	[sudo] password for socketubs: 
	Creating new encrypted volume.
	Please choose from one of the following options:
	 enter "x" for expert configuration mode,
	 enter "p" for pre-configured paranoia mode,
	 anything else, or an empty line will select standard mode.
	?> 

	Standard configuration selected.

	Configuration finished.  The filesystem to be created has
	the following properties:
	Filesystem cipher: "ssl/aes", version 3:0:2
	Filename encoding: "nameio/block", version 3:0:1
	Key Size: 192 bits
	Block Size: 1024 bytes
	Each file contains 8 byte header with unique IV data.
	Filenames encoded using IV chaining mode.
	File holes passed through to ciphertext.

	Now you will need to enter a password for your filesystem.
	You will need to remember this password, as there is absolutely
	no recovery mechanism.  However, the password can be changed
	later using encfsctl.

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
