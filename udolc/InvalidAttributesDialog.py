# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 <Konstantinos Mastorakis> <mastorak at gmail dot com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('udolc')

import logging
logger = logging.getLogger('udolc')

from udolc_lib.ErrorDialog import ErrorDialog

# See udolc_lib.ErrorDialog.py for more details about how this class works.
class InvalidAttributesDialog(ErrorDialog):
    __gtype_name__ = "InvalidAttributesDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the Invalid Attributes dialog"""
        super(ErrorDialog, self).finish_initializing(builder)

       
