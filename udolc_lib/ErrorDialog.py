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

from gi.repository import Gtk # pylint: disable=E0611

from . helpers import get_builder

class ErrorDialog(Gtk.MessageDialog):
    __gtype_name__ = "ErrorDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated ErrorDialog object.
        """
        builder = get_builder('ErrorDialog')
        new_object = builder.get_object("errorDialog")
  
        return new_object

 
