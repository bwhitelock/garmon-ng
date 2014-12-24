#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# chevrolet_codes.py
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
    "P1260": _("Fuel Pump Speed Relay Control Circuit"),
    "P1336": _("Crankshaft Position System Variation Not Learned"),
    "P1351": _("Ignition Coil Control Circuit High Voltage"),
    "P1352": _("Ignition Bypass Circuit High Voltage"),
    "P1361": _("Ignition Control (IC) Circuit Low Voltage"),
    "P1362": _("Ignition Bypass Circuit Low Voltage"),
    "P1374": _("CKP High to Low Resolution Frequency Correlation"),
    "P1380": _("Misfire Detected - Rough Road Data Not Available"),
    "P1381": _("Misfire Detected - No Commun. W/ Brake Control Mod"),
    "P1404": _("EGR Closed Position Performance"),
    "P1415": _("Secondary Air Injection (AIR) System Bank 1"),
    "P1416": _("Secondary Air Injection (AIR) System Bank 2"),
    "P1441": _("Evaporative Emission System Flow During Non-Purge"),
    "P1546": _("Air Conditioning (A/C) Clutch Relay Control Circuit"),
    "P1585": _("Cruise Control Inhibit Output Circuit"),
    "P1624": _("Customer Snapshot Requested - Data Available"),
    "P1635": _("5 Volt Reference Circuit"),
    "P1639": _("5 Volt Reference 2 Circuit"),
    "P1670": _("ODM has Detected a Voltage greater than 33 volts"),
    "P1689": _("Traction Control Delivered Torque Output Circuit"),
    "P1810": _("TFP Valve Position Switch Circuit"),
    "P1811": _("Maximum Adapt and Long Shift"),
    "P1819": _("Internal Mode Switch - No Start/Wrong Range"),
    "P1820": _("Internal Mode Switch Circuit A Low"),
    "P1822": _("Internal Mode Switch Circuit B High"),
    "P1823": _("Internal Mode Switch Circuit P Low"),
    "P1825": _("Internal Mode Switch - Invalid Range"),
    "P1826": _("Internal Mode Switch Circuit C High"),
    "P1860": _("TCC PWM Solenoid Circuit Electrical"),
    "P1887": _("TCC Release Switch Circuit"),
}
