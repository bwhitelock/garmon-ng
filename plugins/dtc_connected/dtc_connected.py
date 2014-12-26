#!/usr/bin/python
#
# dtc_connected.py
#
# Copyright (C) Ben Van Mechelen 2007-2009 <me@benvm.be>
# 
# This file is part of Garmon 
# 
# Garmon is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, write to:
#   The Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor
#   Boston, MA  02110-1301, USA.


from gettext import gettext as _

import gobject
import gtk

import garmon
from garmon.plugin import Plugin
import garmon.obd_device
from garmon.obd_device import OBDPortError

__name = _('DTC Connected')
__version = '0.2'
__author = 'Ben Van Mechelen'
__description = _('illuminates an indicator showing connection status.')
__class = 'DTCConnected'




class DTCConnected (Plugin):
    __gtype_name__='DTCConnected'
    def __init__(self, app):
        Plugin.__init__(self)

        self.app = app
                
        self.ui_info = '''<ui>
                                <toolbar  name='ToolBar'>
                                    <placeholder name='DeviceToolItems'>
                                    <separator/>
                                        <toolitem action='ConnectedDTC'/>
                                    </placeholder>
                                </toolbar>
                            </ui>'''
                            
        self._create_action_group()
        

    def _sensitize_action(self):
        sensitive = self.app.device.connected
        self.app.ui.get_widget('/ToolBar/DeviceToolItems/ConnectedDTC').set_sensitive(sensitive)
        

    def _scheduler_notify_working_cb(self, scheduler, monitoring):
        self._sensitize_action()
        
        
    def _obd_connected_cb(self, obd, connected):
        self._sensitize_action()
        
        
    def _create_action_group(self):
        
        entries = (
            ( 'ConnectedDTC', gtk.STOCK_YES,                     
                _('_Connected DTC'), '',                    
                _('Connection status indicator'), self.activate_connected_dtc ),)
            
        self.action_group = gtk.ActionGroup("ConnectedDTCActionGroup")
        self.action_group.add_actions(entries)
              
        
    def activate_connected_dtc(self, action):
        
        def success_cb(cmd, result, args):
            if result:
                self.app.reset()
        
        def err_cb(cmd, err, args):
            dialog = gtk.MessageDialog(self.app, gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, 
                _("""An error occurred while trying to disconnect.\n
Please make sure your device is connected.
The ignition must be turned on but the engine should not be running"""))
    
            dialog.run()
            dialog.destroy()                    


        dialog = gtk.MessageDialog(self.app, gtk.DIALOG_DESTROY_WITH_PARENT,
                 gtk.MESSAGE_QUESTION, gtk.BUTTONS_OK_CANCEL,
                 _("""Are You Sure You want to disconnect the OBD device?"""))
            
        dialog.show()
        res = dialog.run()
        dialog.destroy()
                
        if res == gtk.RESPONSE_OK:
            try:
                self.app.device.close()
                #MOVE THIS 
            except OBDPortError, e:
                err, msg = e
                dialog = gtk.MessageDialog(self.app, gtk.DIALOG_DESTROY_WITH_PARENT,
                    gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, 
                    err + '\n\n' + msg)
                dialog.run()
                dialog.destroy()
                raise

                
    def load(self):
        self._sensitize_action()
        #self.app.scheduler.connect('notify::working', self._scheduler_notify_working_cb)
        self.app.device.connect('connected', self._obd_connected_cb)
                
                
    def unload(self):
        pass            
        
    def start(self):
        pass
        
    def stop(self):
        pass
        
        
    
