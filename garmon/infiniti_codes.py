#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# infiniti_codes.py
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
    "P1105": _("MAP/BARO Switch Solenoid Valve"),
    "P1110": _("Intake Valve Timing Control (Left Bank)"),
    "P1120": _("Secondary Throttle Position Sensor (STPS)"),
    "P1125": _("TPS Intermittant"),
    "P1130": _("Swirl Control Valve Control Solenoid Valve"),
    "P1135": _("Intake Valve Timing Control (Right Bank)"),
    "P1140": _("Intake Valve Timing Control Position Sensor (Left Bank)"),
    "P1145": _("Intake Valve Timing Control Position Sensor (Right Bank)"),
    "P1148": _("Closed Loop Control (Bank 1)"),
    "P1165": _("Swirl Control Valve Control Vacuum Check Switch"),
    "P1168": _("Closed Loop Control (Bank 2)"),
    "P1210": _("Traction Control System (TCS) Signal Circuit"),
    "P1220": _("Fuel Pump Control Module (FPCM)"),
    "P1320": _("Ignition Signal, Primary"),
    "P1335": _("Crankshaft Position Sensor (CKPS) (Ref)"),
    "P1336": _("Crankshaft Position Sensor (CKPS) (Cog)"),
    "P1400": _("EGRC Solenoid Valve"),
    "P1401": _("EGR Temperature Sensor"),
    "P1402": _("EGR Function (Open)"),
    "P1440": _("EVAP Control System (Small Leak) (Positive Pressure)"),
    "P1441": _("VC/V Bypass Valve"),
    "P1443": _("Canister Control Vacuum Check Switch"),
    "P1444": _("Canister Purge Volume Control Solenoid Valve"),
    "P1445": _("Purge Volume Control/V"),
    "P1446": _("EVAP Canister Vent Control Valve (Close)"),
    "P1447": _("EVAP Control System Purge Flow Monitoring"),
    "P1448": _("EVAP Canister Vent Control Valve (Open)"),
    "P1490": _("Vacuum Cut Valve Bypass Valve (Circuit)"),
    "P1491": _("Vacuum Cut Valve Bypass Valve"),
    "P1492": _("EVAP Canister Purge Control/Solenoid Valve (Circuit)"),
    "P1493": _("EVAP Canister Purge Control Valve/Solenoid Valve"),
    "P1605": _("A/T Diagnosis Communication Line"),
    "P1705": _("Throttle Position Sensor"),
    "P1706": _("PNP Switch"),
    "P1760": _("Overrun Clutch Solenoid Valve"),
    "P1900": _("Cooling Fan"),
}
