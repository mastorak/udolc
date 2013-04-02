# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from gi.repository import Gtk # pylint: disable=E0611

from . helpers import get_builder

class LauncherCreatedDialog(Gtk.MessageDialog):
    __gtype_name__ = "MessageDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated LauncherCreatedDialog object.
        """
        builder = get_builder('LauncherCreatedDialog')
        new_object = builder.get_object("launcherCreatedDialog")
  
        return new_object

 
