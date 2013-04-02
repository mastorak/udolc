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
import os,stat
import gettext
from gettext import gettext as _
gettext.textdomain('udolc')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('udolc')

from udolc_lib import Window

from udolc.AboutUdolcDialog import AboutUdolcDialog
from udolc.InfoDialog import InfoDialog
from udolc.InvalidAttributesDialog import InvalidAttributesDialog


# See udolc_lib.Window.py for more details about how this class works
class UdolcWindow(Window):
    __gtype_name__ = "UdolcWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UdolcWindow, self).finish_initializing(builder)
       
        self.AboutDialog = AboutUdolcDialog
        
       
        statusIcon = Gtk.StatusIcon()
        statusIcon.set_from_file('data/media/udolc.svg')
        statusIcon.set_visible(True)

        # Get widgets
        self.saveBtn=self.builder.get_object("saveBtn")
        self.resetBtn=self.builder.get_object("resetBtn")
        self.nameField=self.builder.get_object("nameField")
        self.commentField=self.builder.get_object("commentField")
        self.execField=self.builder.get_object("execField")
        self.iconSelect=self.builder.get_object("iconSelect")
        self.terminalCheckbox=self.builder.get_object("terminalCheckbox")
        self.typeCombo=self.builder.get_object("typeCombo")

        #Initialise widgets
        self.iconSelect.set_filename("/usr/share/udolc/media/default_icon.png")
        self.typeCombo.set_active(0) 
       
        
        
    def on_saveBtn_clicked(self,widget):        
        print "Saving laucher"        
        name=self.nameField.get_text()
        comment=self.commentField.get_text()
        if comment=="":
            comment=name
            
        executable=self.execField.get_text()
        icon=self.iconSelect.get_filename()
        launcherType=self.typeCombo.get_active_text()
        terminalCheck=self.terminalCheckbox.get_active()
        isTerminal="false"        
        if terminalCheck:
            isTerminal="true"
            
                            
        
        if name=="" or executable=="":
            print "Invalid Arguments"
            error=InvalidAttributesDialog()
            error.show()
            return               
        else:
            homeDir=os.getenv("HOME")
            copyDir=homeDir+"/.local/share/applications/"
            fileName=copyDir+name+".desktop"           
            f = open(fileName, 'w')
            f.write("[Desktop Entry]\n")
            f.write("Type=Application\n")
            f.write("Name="+name+"\n")
            f.write("Comment="+comment+"\n")
            f.write("Exec="+executable+"\n")
            f.write("Icon="+icon+"\n")
            f.write("Terminal="+isTerminal+"\n")
            f.write("Categories="+launcherType+";\n")
            f.close()
            os.chmod(fileName, stat.S_IRWXU)
            info=InfoDialog()
            os.system("xdg-open "+copyDir)
            info.show()
       

    def on_resetBtn_clicked(self,widget):
        self.nameField.set_text("")
        self.commentField.set_text("")
        self.execField.set_text("")
        self.iconSelect.set_filename("/usr/share/udolc/media/default_icon.png")
        self.typeCombo.set_active(0) 
        

