This is a quick custom grain that you can add to your Salt system to
check your systems for vulnerability to the Shellshock bug
(CVE-2014-6271 and CVE-2014-7169).

To use it, place a copy of shellshock.py in /srv/salt/_grains and then run:

    salt '*' saltutil.sync_grains

Once that has run, you should be able to tell which of your systems is
vulnerable by running:

    salt '*' grains.item shellshock

To see if your systems are specifically vulnerable to CVE-2014-6271, run:

    salt '*' grains.item shellshock1

To see if your systems are specifically vulnerable to CVE-2014-7169, run:

    salt '*' grains.item shellshock2
