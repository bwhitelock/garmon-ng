#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# toyota_codes.py
#
# Copyright (C) Ben Van Mechelen 2008-2009 <me@benvm.be>
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

DTC_CODES_MANUFACTURER = {
    "P1100": _("BARO Sensor Circuit."),
    "P1120": _("Accelerator Pedal Position Sensor Circuit."),
    "P1121": _("Accelerator Pedal Position Sensor Range/Performance Problem."),
    "P1125": _("Throttle Control Motor Circuit."),
    "P1126": _("Magnetic Clutch Circuit."),
    "P1127": _("ETCS Actuator Power Source Circuit."),
    "P1128": _("Throttle Control Motor Lock."),
    "P1129": _("Electric Throttle Control System."),
    "P1130": _("Air/Fuel Sensor Circuit Range/Performance. (Bank 1 Sensor 1)"),
    "P1133": _("Air/Fuel Sensor Circuit Response. (Bank 1 Sensor 1)"),
    "P1135": _("Air/Fuel Sensor Heater Circuit Response. (Bank 1 Sensor 1)"),
    "P1150": _("Air/Fuel Sensor Circuit Range/Performance. (Bank 1 Sensor 2)"),
    "P1153": _("Air/Fuel Sensor Circuit Response. (Bank 1 Sensor 2)"),
    "P1155": _("Air/Fuel Sensor Heater Circuit. (Bank 1 Sensor 2)"),
    "P1200": _("Fuel Pump Relay Circuit."),
    "P1300": _("Igniter Circuit Malfunction - No. 1."),
    "P1310": _("Igniter Circuit Malfunction - No. 2."),
    "P1335": _("No Crankshaft Position Sensor Signal - Engine Running."),
    "P1349": _("VVT System."),
    "P1400": _("Sub-Throttle Position Sensor."),
    "P1401": _("Sub-Throttle Position Sensor Range/Performance Problem."),
    "P1405": _("Turbo Pressure Sensor Circuit."),
    "P1406": _("Turbo Pressure Sensor Range/Performance Problem."),
    "P1410": _("EGR Valve Position Sensor Circuit Malfunction."),
    "P1411": _("EGR Valve Position Sensor Circuit Range/Performance."),
    "P1500": _("Starter Signal Circuit."),
    "P1510": _("Boost Pressure Control Circuit."),
    "P1511": _("Boost Pressure Low."),
    "P1512": _("Boost Pressure High."),
    "P1520": _("Stop Lamp Switch Signal Malfunction."),
    "P1565": _("Cruise Control Main Switch Circuit."),
    "P1600": _("ECM BATT Malfunction"),
    "P1605": _("Knock Control CPU."),
    "P1630": _("Traction Control System."),
    "P1633": _("ECM."),
    "P1652": _("Idle Air Control Valve Control Circuit."),
    "P1656": _("OCV Circuit."),
    "P1658": _("Wastegate Valve Control Circuit."),
    "P1661": _("EGR Circuit."),
    "P1662": _("EGR by-pass Valve Control Circuit."),
    "P1780": _("Park/Neutral Position Switch Malfunction (Only For A/T)"),
    "P1875": _("4WD Low Switch Circuit Malfunction"),
}
