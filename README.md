This is a quick custom grain that you can add to your Salt system to check your
systems for vulnerability to the Shellshock bug.

To use it, place a copy of shellshock.py in /srv/salt/_grains and then run:

    salt '*' saltutil.sync_grains

Once that has run, you should be able to tell which of your systems is
vulnerable by running:

    salt '*' grains.item shellshock
