#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# lexus_codes.py
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
    "P1100": _("BARO Sensor Circuit Malfunction"),
    "P1120": _("Accelerator Pedal Position Sensor Circuit Malfunction"),
    "P1121": _("Accelerator Pedal Position Sensor Range/Performance Problem"),
    "P1125": _("Throttle Control Motor Circuit Malfunction"),
    "P1126": _("Magnetic Clutch Circuit Malfunction"),
    "P1127": _("ECTS Actuator Power Source Circuit Malfunction"),
    "P1128": _("Throttle Control Motor Lock Malfunction"),
    "P1129": _("Electronic Throttle Control System"),
    "P1130": _("Air/Fuel Ratio Sensor Circuit Range/Performance Malfunction (Bank 1 Sensor 1)"),
    "P1133": _("Air/Fuel Ratio Sensor Circuit Response Malfunction (Bank 1 Sensor 1)"),
    "P1135": _("Air/Fuel Ratio Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)"),
    "P1150": _("Air/Fuel Ratio Sensor Circuit Range/Performance Malfunction (Bank 2 Sensor 1)"),
    "P1153": _("Air/Fuel Ratio Sensor Circuit Response Malfunction (Bank 2 Sensor 1)"),
    "P1155": _("Air/Fuel Ratio Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)"),
    "P1200": _("Fuel Pump Relay/ECU Circuit Malfunction"),
    "P1300": _("Igniter Circuit Malfunction (Bank 1 Or No. 1)"),
    "P1305": _("Igniter Circuit Malfunction, (Bank 2 Or No. 2)"),
    "P1310": _("Igniter Circuit Malfunction (No. 3)"),
    "P1315": _("Igniter Circuit Malfunction (No. 4)"),
    "P1320": _("Igniter Circuit Malfunction (No. 5)"),
    "P1325": _("Igniter Circuit Malfunction (No. 6)"),
    "P1330": _("Igniter Circuit Malfunction (No. 7)"),
    "P1335": _("CKP Sensor Circuit Malfunction During Engine Running"),
    "P1340": _("Igniter Circuit Malfunction (No. 8)"),
    "P1345": _("VVT Sensor Circuit Malfunction (Bank 1)"),
    "P1346": _("VVT Sensor Rang/Performance Problem (Bank 1)"),
    "P1349": _("VVT System Malfunction (Bank 1)"),
    "P1350": _("VVT Sensor Circuit Malfunction (Bank 2)"),
    "P1351": _("VVT Sensor Range/Performance Problem (Bank 2)"),
    "P1354": _("VVT System Malfunction (Bank 2)"),
    "P1400": _("Sub-TP Sensor Malfunction"),
    "P1401": _("Sub-TP Sensor Range/Performance"),
    "P1410": _("EGR Valve Position Sensor Circuit Malfunction"),
    "P1411": _("EGR Valve Position Sensor Circuit Range/Performance Malfunction"),
    "P1500": _("Starter Signal Circuit Malfunction"),
    "P1520": _("Stop Lamp Switch Malfunction"),
    "P1565": _("Cruise Control Main Switch Circuit Malfunction"),
    "P1566": _("Cruise Control Main Switch Circuit Malfunction"),
    "P1600": _("ECM BATT Malfunction"),
    "P1605": _("Knock Control CPU Malfunction"),
    "P1633": _("ECM Malfunction (ETCS Circuit)"),
    "P1645": _("Body ECU Malfunction"),
    "P1656": _("OCV Circuit Malfunction (Bank 1)"),
    "P1663": _("OCV Circuit Malfunction (Bank 2)"),
    "P1780": _("PNP Switch Malfunction"),
    "B2785": _("Ignition Switch On Malfunction (Immobilizer System)"),
    "B2786": _("Ignition Switch Off Malfunction (Immobilizer System)"),
    "B2785": _("Ignition Switch On Malfunction (Immobilizer System)"),
    "B2791": _("Key Unlock Warning Switch Malfunction (Immobilizer System)"),
    "B2795": _("Unmatch Key Code (Immobilizer System)"),
    "B2796": _("No Communication In Immobilizer System"),
    "B2797": _("Communication Malfunction No. 1 (Immobilizer System)"),
    "B2798": _("Communication Malfunction No. 2 (Immobilizer System)"),
}
