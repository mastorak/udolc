#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

###################### DO NOT TOUCH THIS (HEAD TO THE SECOND PART) ######################

import os
import sys

try:
    import DistUtilsExtra.auto
except ImportError:
    print >> sys.stderr, 'To build udolc you need https://launchpad.net/python-distutils-extra'
    sys.exit(1)
assert DistUtilsExtra.auto.__version__ >= '2.18', 'needs DistUtilsExtra.auto >= 2.18'

def update_config(values = {}):

    oldvalues = {}
    try:
        fin = file('udolc_lib/udolcconfig.py', 'r')
        fout = file(fin.name + '.new', 'w')

        for line in fin:
            fields = line.split(' = ') # Separate variable from value
            if fields[0] in values:
                oldvalues[fields[0]] = fields[1].strip()
                line = "%s = %s\n" % (fields[0], values[fields[0]])
            fout.write(line)

        fout.flush()
        fout.close()
        fin.close()
        os.rename(fout.name, fin.name)
    except (OSError, IOError), e:
        print ("ERROR: Can't find udolc_lib/udolcconfig.py")
        sys.exit(1)
    return oldvalues


def update_desktop_file(datadir):

    try:
        fin = file('udolc.desktop.in', 'r')
        fout = file(fin.name + '.new', 'w')

        for line in fin:            
            if 'Icon=' in line:
                line = "Icon=%s\n" % (datadir + 'media/udolc.svg')
            fout.write(line)
        fout.flush()
        fout.close()
        fin.close()
        os.rename(fout.name, fin.name)
    except (OSError, IOError), e:
        print ("ERROR: Can't find udolc.desktop.in")
        sys.exit(1)


class InstallAndUpdateDataDirectory(DistUtilsExtra.auto.install_auto):
    def run(self):
        values = {'__udolc_data_directory__': "'%s'" % (self.prefix + '/share/udolc/'),
                  '__version__': "'%s'" % self.distribution.get_version()}
        previous_values = update_config(values)
        update_desktop_file(self.prefix + '/share/udolc/')
        DistUtilsExtra.auto.install_auto.run(self)
        update_config(previous_values)


        
##################################################################################
###################### YOU SHOULD MODIFY ONLY WHAT IS BELOW ######################
##################################################################################

DistUtilsExtra.auto.setup(
    name='udolc',
    version='0.1',
    license='GPL v3',
    author='Konstantinos Mastorakis',
    author_email='mastorak@gmail.com',
    description='Utility to create application launchers for Ubuntu Unity',
    long_description='Udolc creates launchers that can be run from Ubuntu Unity dock and stores them in your ~/.local/share/applications/ folder ',
    url='http://github.com/mastorak/udolc',
    cmdclass={'install': InstallAndUpdateDataDirectory}
    )

