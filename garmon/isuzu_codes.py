#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# isuzu_codes.py
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
    "P1106": _("MAP Circuit Intermittent Voltage High"),
    "P1107": _("MAP Circuit Intermittent Voltage Low"),
    "P1108": _("Barometric Pressure Circuit Input High"),
    "P1111": _("IAT Sensor Circuit Intermittent Voltage High"),
    "P1112": _("IAT Sensor Circuit Intermittent Voltage Low"),
    "P1114": _("ECT Sensor Circuit Intermittent Voltage Low"),
    "P1115": _("ECT Sensor Circuit Intermittent Voltage High"),
    "P1121": _("TP Sensor Circuit Intermittent Voltage High"),
    "P1122": _("TP Sensor Circuit Intermittent Voltage Low"),
    "P1133": _("H02S Insufficient Switching Bank 1 Sensor 1"),
    "P1134": _("H02S Transition Time Ratio Bank 1 Sensor 1"),
    "P1153": _("H02S Insufficient Switching Bank 2 Sensor 1"),
    "P1154": _("H02S Transition Time Ratio Bank 2 Sensor 1"),
    "P1171": _("Fuel System Lean During Acceleration"),
    "P1297": _("Electrical Load Detector Circuit Input Low"),
    "P1298": _("Electrical Load Detector Circuit Input High"),
    "P1300": _("Random Misfire"),
    "P1336": _("CKP System Variation Not Learned"),
    "P1359": _("CKP/TDC Sensor Disconnected"),
    "P1361": _("TDC Sensor Intermittent Interruption"),
    "P1362": _("TDC Sensor No Signal"),
    "P1380": _("ABS Rough Road System Fault"),
    "P1381": _("Cylinder Position Sensor Intermittent Interruption, Misfire Detected (Except 1998 Rodeo)"),
    "P1381": _("ABS Rough Road Class 2 Serial Data Fault Or Link Error (1998 Rodeo)"),
    "P1382": _("Cylinder Position Sensor No Signal"),
    "P1390": _("G Sensor Circuit Intermittent Voltage Low"),
    "P1391": _("G Sensor Performance"),
    "P1392": _("G Sensor Voltage Low"),
    "P1393": _("G Sensor Voltage High"),
    "P1394": _("G Sensor Intermittent Voltage High"),
    "P1404": _("EGR Valve Stuck Closed"),
    "P1406": _("EGR Valve Pintle Position Circuit"),
    "P1441": _("EVAP System Flow During Non-Purge"),
    "P1442": _("EVAP Vacuum Switch Voltage High During Ignition On"),
    "P1459": _("EVAP Emission Purge Flow Switch Malfunction"),
    "P1491": _("EGR Valve Lift Insufficient Detected"),
    "P1498": _("EGR Valve Lift Sensor Voltage High"),
    "P1508": _("IAC System RPM Low"),
    "P1509": _("IAC System RPM High"),
    "P1546": _("A/C Compressor Clutch Output Circuit Malfunction"),
    "P1548": _("A/C Compressor Clutch Output Circuit Malfunction"),
    "P1607": _("PCM Internal Circuit Failure ‘‘A’’"),
    "P1618": _("SPI Communications Error"),
    "P1625": _("PCM Unexpected Reset"),
    "P1627": _("PCM A/D Conversion Malfunction"),
    "P1635": _("5 Volt Reference Voltage Circuit Malfunction"),
    "P1640": _("ODM 1 Input Voltage High (Except 1998 Rodeo)"),
    "P1640": _("ODM Output ‘‘A’’ Circuit Fault (1998 Rodeo)"),
    "P1650": _("Quad Driver Module ‘‘A’’ Fault"),
    "P1790": _("Trans ROM Checksum Error"),
    "P1792": _("Trans EEPROM Checksum Error"),
    "P1835": _("Trans Kickdown Switch Malfunction"),
    "P1850": _("Brake Band Apply Solenoid Malfunction"),
    "P1860": _("TCC PWM Solenoid Circuit Failure"),
    "P1870": _("Transmission Component Slipping"),
}
