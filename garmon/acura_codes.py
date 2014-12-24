#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# acura_codes.py
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
    "P1106": _("BARO Sensor Circuit Range/Performance Malfunction"),
    "P1107": _("BARO Circuit Low Input"),
    "P1108": _("BARO Circuit High Input"),
    "P1121": _("Throttle Position Lower Than Expected"),
    "P1122": _("Throttle Position Higher Than Expected"),
    "P1128": _("MAP Lower Than Expected"),
    "P1129": _("MAP Higher Than Expected"),
    "P1259": _("VTEC System Malfunction"),
    "P1297": _("ELD Circuit Low Input"),
    "P1298": _("ELD Circuit High Input"),
    "P1300": _("Random Misfire"),
    "P1336": _("Crankshaft Speed Fluctuation Sensor Intermittant Interruption"),
    "P1337": _("Crankshaft Speed Fluctuation Sensor No Signal"),
    "P1359": _("Crankshaft Position/TDC/Cylinder Position Sensor Connector Disconnection"),
    "P1361": _("TDC Sensor Intermittent Interruption"),
    "P1362": _("TDC 1 Sensor No Signal"),
    "P1366": _("TDC 2 Sensor Intermittent"),
    "P1367": _("TDC 2 Sensor No Signal"),
    "P1381": _("Cylinder Position Sensor Intermittant Inturruption"),
    "P1382": _("Cylinder Position Sensor No Signal"),
    "P1456": _("EVAP System Leak Detected (Fuel Tank System)"),
    "P1457": _("EVAP Control System Leak Detected (Control Canister System)"),
    "P1491": _("EGR Valve Lift Insufficient Detected"),
    "P1498": _("Voltage Problem In EGR Valve Position Sensor Circuit"),
    "P1508": _("Idle Air Control Valve Circuit Failure"),
    "P1519": _("IAC Valve Circuit Failure"),
    "P1607": _("ECM/PCM Internal Circuit Failure"),
    "P1656": _("Automatic Transaxle"),
    "P1660": _("A/T FI Data Line Failure"),
    "P1676": _("FPTDR Signal Line Failure"),
    "P1678": _("FPTDR Signal Line Failure"),
    "P1681": _("A/T FI Signal A Low Input"),
    "P1682": _("A/T FI Signal A High Input"),
    "P1686": _("A/T FI Signal B Low Input"),
    "P1687": _("A/T FI Signal B High Input"),
    "P1705": _("Automatic Transaxle"),
    "P1706": _("Automatic Transaxle"),
    "P1709": _("Automatic Transaxle"),
    "P1710": _("Automatic Transaxle"),
    "P1713": _("Automatic Transaxle"),
    "P1738": _("Automatic Transaxle"),
    "P1739": _("Automatic Transaxle"),
    "P1740": _("Automatic Transaxle"),
    "P1753": _("Automatic Transaxle"),
    "P1758": _("Automatic Transaxle"),
    "P1768": _("Automatic Transaxle"),
    "P1773": _("Automatic Transaxle"),
    "P1778": _("Automatic Transaxle"),
    "P1786": _("Automatic Transaxle"),
    "P1790": _("Automatic Transaxle"),
    "P1791": _("Automatic Transaxle"),
    "P1792": _("Automatic Transaxle"),
    "P1794": _("Automatic Transaxle"),
}
