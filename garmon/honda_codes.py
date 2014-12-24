#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# honda_codes.py
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
    "P1106": _("Barometric Pressure Circuit Range/Performance"),
    "P1107": _("Barometric Pressure Circuit Low Input"),
    "P1108": _("Barometric Pressure Circuit High Input"),
    "P1121": _("Throttle Position Lower Than Expected"),
    "P1122": _("Throttle Position Higher Than Expected"),
    "P1128": _("MAP Lower Than Expected"),
    "P1129": _("MAP Higher Than Expected"),
    "P1149": _("Primary HO2S (Sensor 1) Circuit Range/Performance Problem"),
    "P1162": _("Primary HO2S (No. 1) Circuit Malfunction"),
    "P1163": _("Primary HO2S (No. 1) Circuit Slow Response"),
    "P1164": _("Primary HO2S (No. 1) Circuit Range/Performance"),
    "P1165": _("Primary HO2S (No. 1) Circuit Range/Performance"),
    "P1166": _("Primary HO2S (No. 1) Heater System Electrical"),
    "P1167": _("Primary HO2S (No. 1) Heater System"),
    "P1168": _("Primary HO2S (No. 1) LABEL Low Input"),
    "P1169": _("Primary HO2S (No. 1) LABEL High Input"),
    "P1253": _("VTEC System Malfunction"),
    "P1257": _("VTEC System Malfunction"),
    "P1258": _("VTEC System Malfunction"),
    "P1259": _("VTEC System Malfunction"),
    "P1297": _("Electrical Load Detector Circuit Low Input"),
    "P1298": _("Electrical Load Detector Circuit High Input"),
    "P1300": _("Multiple Cylinder Misfire Detected"),
    "P1336": _("CSF Sensor Intermittent Interruption"),
    "P1337": _("CSF Sensor No Signal"),
    "P1359": _("CKP/TDC Sensor Connector Disconnection"),
    "P1361": _("Intermittent Interruption In TDC 1 Sensor Circuit"),
    "P1362": _("No Signal In TDC 1 Sensor Circuit"),
    "P1366": _("Intermittent Interruption In TDC 2 Sensor Circuit"),
    "P1367": _("No Signal In TDC 2 Sensor Circuit"),
    "P1381": _("Cylinder Position Sensor Intermittent Interruption"),
    "P1382": _("Cylinder Position Sensor No Signal"),
    "P1456": _("EVAP Emission Control System Leak Detected (Fuel Tank System)"),
    "P1457": _("EVAP Emission Control System Leak Detected (Control Canister System)"),
    "P1459": _("EVAP Emission Purge Flow Switch Malfunction"),
    "P1486": _("Thermostat Range/Performance Problem"),
    "P1491": _("EGR Valve Lift Insufficient Detected"),
    "P1498": _("EGR Valve Lift Sensor High Voltage"),
    "P1508": _("IAC Valve Circuit Failure"),
    "P1509": _("IAC Valve Circuit Failure"),
    "P1519": _("Idle Air Control Valve Circuit Failure"),
    "P1607": _("ECM/PCM Internal Circuit Failure A"),
    "P1655": _("SEAF/SEFA/TMA/TMB Signal Line Failure"),
    "P1656": _("Automatic Transaxle"),
    "P1660": _("Automatic Transaxle FI Signal A Circuit Failure"),
    "P1676": _("FPTDR Signal Line Failure"),
    "P1678": _("FPTDR Signal Line Failure"),
    "P1681": _("Automatic Transaxle FI Signal A Low Input"),
    "P1682": _("Automatic Transaxle FI Signal A High Input"),
    "P1686": _("Automatic Transaxle FI Signal B Low Input"),
    "P1687": _("Automatic Transaxle FI Signal B High Input"),
    "P1705": _("Automatic Transaxle Concerns"),
    "P1706": _("Automatic Transaxle Concerns"),
    "P1738": _("Automatic Transaxle Concerns"),
    "P1739": _("Automatic Transaxle Concerns"),
    "P1753": _("Automatic Transaxle Concerns"),
    "P1758": _("Automatic Transaxle Concerns"),
    "P1768": _("Automatic Transaxle Concerns"),
    "P1773": _("Automatic Transaxle Concerns"),
    "P1785": _("Automatic Transaxle Concerns"),
    "P1786": _("Automatic Transaxle Concerns"),
    "P1790": _("Automatic Transaxle Concerns"),
    "P1791": _("Automatic Transaxle Concerns"),
    "P1792": _("Automatic Transaxle Concerns"),
    "P1793": _("Automatic Transaxle Concerns"),
    "P1794": _("Automatic Transaxle Concerns"),
    "P1870": _("Automatic Transaxle Concerns"),
    "P1873": _("Automatic Transaxle Concerns"),
    "P1879": _("Automatic Transaxle Concerns"),
    "P1885": _("Automatic Transaxle Concerns"),
    "P1886": _("Automatic Transaxle Concerns"),
    "P1888": _("Automatic Transaxle Concerns"),
    "P1890": _("Automatic Transaxle Concerns"),
    "P1891": _("Automatic Transaxle Concerns"),
}
