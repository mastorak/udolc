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

import gettext
from gettext import gettext as _
gettext.textdomain('udolc')

import logging
logger = logging.getLogger('udolc')

from udolc_lib.LauncherCreatedDialog import LauncherCreatedDialog

# See udolc_lib.LauncherCreatedDialog.py for more details about how this class works.
class InfoDialog(LauncherCreatedDialog):
    __gtype_name__ = "InfoDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the info dialog"""
        super(LauncherCreatedDialog, self).finish_initializing(builder)

    
