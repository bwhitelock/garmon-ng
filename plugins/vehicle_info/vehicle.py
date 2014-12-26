#!/usr/bin/python
#
# vehicle.py
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

import os

import gobject
from gobject import GObject
import gtk
from gtk import glade
from gettext import gettext as _

import garmon
import garmon.plugin

from garmon.plugin import Plugin, STATUS_STOP, STATUS_WORKING, STATUS_PAUSE
from garmon.property_object import PropertyObject, gproperty
from garmon.obd_device import OBDDataError, OBDPortError
#from garmon.trouble_codes import DTC_CODES, DTC_CODE_CLASSES
from garmon.trouble_codes import *
from garmon.sensor import decode_dtc_code

__name = _('Vehicle')
__version = '0.2'
__author = 'Ben Van Mechelen'
__description = _('Vehicle information')
__class = 'Vehicle'


class Vehicle (gtk.VBox, Plugin):
    __gtype_name__='Vehicle'
    def __init__(self, app):
        gtk.VBox.__init__(self)
        Plugin.__init__(self)
        
        self.app = app
        self.dir = os.path.dirname(__file__)
        self.status = STATUS_STOP
        
        fname = os.path.join(self.dir, 'vehicle.glade')
        self._glade = glade.XML(fname, 'vehicle_info_box')
        main_vbox = self._glade.get_widget('vehicle_info_box')
        self.pack_start(main_vbox)
        main_vbox.show_all()

        self._vehicle_name = self._glade.get_widget('vehicle_name_data')
        self._vehicle_plate = self._glade.get_widget('vehicle_plate_data')
        self._vehicle_make = self._glade.get_widget('vehicle_make_data')
        self._vehicle_model = self._glade.get_widget('vehicle_model_data')
        self._vehicle_year = self._glade.get_widget('vehicle_year_data')
        self._vehicle_vin = self._glade.get_widget('vehicle_vin_data')
        self._vehicle_engine = self._glade.get_widget('vehicle_engine_data')
        self._vehicle_fuel = self._glade.get_widget('vehicle_fuel_data')
        self._vehicle_obd = self._glade.get_widget('vehicle_obd_data')
        self._vehicle_last_connect = self._glade.get_widget('vehicle_last_connect_data')

        alignment = gtk.Alignment(0, 0, 0, 0)
        self.layout = gtk.Layout()
        alignment.add(self.layout)
        self.pack_start(alignment, True, True)
        self.show_all()
        
        self._reset_cbid = app.connect("reset", self._on_reset)
        self._switch_cbid = app.notebook.connect('switch-page', 
                                              self._notebook_page_change_cb)


    def _on_reset(self, app):
        self.start()


    def _reread_button_clicked(self, app):
        self.start()


    def _notebook_page_change_cb (self, notebook, no_use, page):
        plugin = notebook.get_nth_page(page)
        if plugin is self:
            self.app.set_active_plugin(plugin)
            self.start()
        else:
            self.stop()


    def restart(self):
        self.stop()
        self.start()


    def stop(self):
        pass
        

    def start(self):
        self.current_make = self.app.prefs.get("vehicle.make")
        self._vehicle_name.set_text(self.app.prefs.get("vehicle.name"))
        self._vehicle_plate.set_text(self.app.prefs.get("vehicle.plate"))
        self._vehicle_make.set_text(self.current_make)
        self._vehicle_model.set_text(self.app.prefs.get("vehicle.model"))
        if int(self.app.prefs.get("vehicle.year")) > 0:
            self._vehicle_year.set_text(str(self.app.prefs.get("vehicle.year")))
        else:
            self._vehicle_year.set_text("")
        self._vehicle_vin.set_text("Unknown")
        self._vehicle_engine.set_text(self.app.prefs.get("vehicle.engine"))
        self._vehicle_fuel.set_text(self.app.prefs.get("vehicle.fuel"))
        self._vehicle_obd.set_text("Unknown")
        self._vehicle_last_connect.set_text("Unknown")

    def load(self):
        self.app.notebook.append_page(self, gtk.Label(_('Vehicle Info')))
                
                
    def unload(self):
        self.app.notebook.disconnect(self._switch_cbid)    
        self.app.disconnect(self._reset_cbid)
        self.app.notebook.remove(self)
        

