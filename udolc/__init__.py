# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
#
#Copyright 2013 Konstantinos Mastorakis
#
#This file is part of Udolc.
#
#UDoLC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at #your option) any later version.
#
#UDoLC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public #License for more details.
#
#You should have received a copy of the GNU General Public License along with UDoLC. If not, see http://www.gnu.org/licenses/
#
### END LICENSE

import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('udolc')

from gi.repository import Gtk # pylint: disable=E0611

from udolc import UdolcWindow

from udolc_lib import set_up_logging, get_version

def parse_options():
    """Support for command line options"""
    parser = optparse.OptionParser(version="%%prog %s" % get_version())
    parser.add_option(
        "-v", "--verbose", action="count", dest="verbose",
        help=_("Show debug messages (-vv debugs udolc_lib also)"))
    (options, args) = parser.parse_args()

    set_up_logging(options)

def main():
    'constructor for your class instances'
    parse_options()

    # Run the application.    
    window = UdolcWindow.UdolcWindow()
    window.show()
    Gtk.main()
