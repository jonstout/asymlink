#!/usr/bin/python

import argparse
import json
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", default=False, action="store_true", help="force symlink creation")

    args   = parser.parse_args()
    config = None

    try:
        with open(".asymlink", "r") as f:
            config = json.load(f)
    except IOError as e:
        print "Could not find .asymlink in this directory."
        exit(1)

    # Pre-existing files and directories that are not symlinks are not
    # overridden without use of the force option.
    if args.force:
        print "Skipping validation; Existing files and directories specified in .asymlink.json will be overridden."
    else:
        ok = True
        for symlink in config.values():
            if os.path.lexists(symlink) and not os.path.islink(symlink):
                ok = False
                print "{0} already exists and is not a symlink. Please backup this file and then remove it.".format(symlink)
        if not ok:
            print "You may also run 'asymlink -f' to force symlink creation."
            exit(1)

    for relative, symlink in config.iteritems():
        local = "{0}/{1}".format(os.getcwd(), relative)

        # Existing symlinks are replaced without warning
        if os.path.lexists(symlink) and os.path.islink(symlink):
            os.unlink(symlink)

        # print local, symlink
        os.symlink(local, symlink)
