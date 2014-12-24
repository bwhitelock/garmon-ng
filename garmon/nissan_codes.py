#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# nissan_codes.py
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
    "P1105": _("MAP/BARO Pressure Switch Solenoid Valve"),
    "P1126": _("Thermostat Function"),
    "P1130": _("Swirl Control Valve Control Solenoid Valve"),
    "P1148": _("Closed Loop Control (Bank 1)"),
    "P1165": _("Swirl Control Valve Control Vacuum Switch"),
    "P1168": _("Closed Loop Control (Bank 2)"),
    "P1320": _("Ignition Signal"),
    "P1211": _("ABS/TCS Control Unit"),
    "P1212": _("ABS/TCS Communication Line"),
    "P1217": _("Engine Over Temperature (Overheat)"),
    "P1320": _("Ignition Signal"),
    "P1335": _("Crankshaft Position Sensor (REF)"),
    "P1336": _("Crankshaft Position Sensor (CKPS)"),
    "P1400": _("EGRC Solenoid Valve"),
    "P1401": _("EGR Temperature Sensor"),
    "P1402": _("EGR System"),
    "P1440": _("EVAP Control System Small Leak"),
    "P1441": _("Vacuum Cut Valve Bypass Valve"),
    "P1444": _("Canister Purge Volume Control Solenoid Valve"),
    "P1445": _("EVAP Canister Purge Volume Control Valve"),
    "P1446": _("EVAP Canister Vent Control Valve (Closed)"),
    "P1447": _("EVAP Control System Purge Flow Monitoring"),
    "P1448": _("EVAP Canister Vent Control Valve (Open)"),
    "P1464": _("Fuel Level Sensor Circuit (Ground Signal)"),
    "P1490": _("Vacuum Cut Valve Bypass Valve (Circuit)"),
    "P1491": _("Vacuum Cut Valve Bypass Valve"),
    "P1492": _("EVAP Canister Purge Control/Solenoid Valve (Circuit)"),
    "P1493": _("EVAP Canister Purge Control Valve/Solenoid Valve"),
    "P1550": _("TCC Solenoid Valve"),
    "P1605": _("A/T Diagnostic Communication Line"),
    "P1705": _("Throttle Position Sensor Circuit A/T"),
    "P1706": _("Park/Neutral Position (PNP) Switch"),
    "P1760": _("Overrun Clutch Solenoid Valve (Circuit)"),
}
