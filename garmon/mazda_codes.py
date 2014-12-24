#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# mazda_codes.py
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
    "P1100": _("MAF Intermittant"),
    "P1101": _("MAF Out Of Range"),
    "P1116": _("ECT Sensor Out Of Range"),
    "P1117": _("ECT Intermittent"),
    "P1120": _("TPS Out Of Range Low"),
    "P1124": _("TPS Out Of Self Test Range"),
    "P1125": _("Tandem Throttle Position Sensor"),
    "P1129": _("Downstream O2 Sensors Swapped Bank To Bank (HO2S-12-22)"),
    "P1130": _("Heated O2 Sensor (HO2S) 11 At Adaptive Limit"),
    "P1131": _("HO2S 11 Indicates Lean"),
    "P1132": _("HO2S 11 Indicates Rich"),
    "P1260": _("Theft Detected - Engine Disabled"),
    "P1270": _("Vehicle Speed Limiter Reached"),
    "P1390": _("Octane Adjust Out Of Range"),
    "P1400": _("DPFE Sensor Low Voltage"),
    "P1401": _("DPFE Sensor High Voltage"),
    "P1403": _("DPFE Hoses Reversed"),
    "P1405": _("DPFE Upstream Hose Off Or Plugged"),
    "P1406": _("DPFE Downstream Hose Off Or Plugged"),
    "P1407": _("EGR No Flow Detected"),
    "P1408": _("EGR Out Of Self Test Range"),
    "P1409": _("EGR Vacuum Regulator Solenoid Circuit Malfunction"),
    "P1443": _("Evaporative Emission Control System"),
    "P1444": _("Purge Flow Sensor Low Input"),
    "P1445": _("Purge Flow Sensor High Input"),
    "P1460": _("WOT A/C Cutoff Circuit Malfunction"),
    "P1500": _("Vehicle Speed Sensor (VSS) Intermittant"),
    "P1505": _("Idle Air Control At Adaptive Clip"),
    "P1506": _("Idle Air Control System Overspeed Error"),
    "P1507": _("Idle Air Control System Underspeed Error"),
    "P1605": _("Powertrain Control Module"),
    "P1650": _("Power Steering Pressure Switch Out Of Range"),
    "P1651": _("Power Steering Pressure Switch Input Malfunction"),
    "P1701": _("Transmission Solenoid Malfunction"),
    "P1703": _("Brake On/Off Switch"),
    "P1705": _("Transmisson Range Sensor"),
    "P1709": _("Park/Neutral Position Switch Out Of Range"),
    "P1711": _("Transmission Fluid Temperature Sensor"),
    "P1729": _("4x4 Low Switch Malfunction"),
    "P1746": _("EPC Solenoid Failed Low"),
    "P1747": _("EPC Solenoid Short Circuit"),
    "P1749": _("EPC Solenoid Open Circuit"),
    "P1751": _("Shift Solenoid #1 (SS1)"),
    "P1754": _("Coast Clutch Solenoid"),
    "P1756": _("Shift Solenoid #2 (SS2)"),
    "P1761": _("Shift Solenoid #3 (SS3)"),
    "P1780": _("Transmission Control Switch"),
    "P1781": _("4x4 Switch Out Of Range"),
    "P1783": _("Transmission Over Temperature Condition"),
}
