#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# kia_codes.py
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
    "P1115": _("Engine Coolant Temperature Signal from ECM to TCM."),
    "P1121": _("Throttle Position Sensor Signal Malfunction from ECM to TCM."),
    "P1170": _("Front Heated Oxygen Sensor Stuck."),
    "P1195": _("EGR Pressure Sensor (1.6L) or Boost Sensor (1.8L) Open or Short."),
    "P1196": _("Ignition Switch ""Start"" Open or Short (1.6L)."),
    "P1250": _("Pressure Regulator Control Solenoid Valve Open or Short."),
    "P1252": _("Pressure Regulator Control Solenoid Valve No. 2 Circuit Malfunction."),
    "P1307": _("Chassis Acceleration Sensor Signal Malfunction."),
    "P1308": _("Chassis Acceleration Sensor Signal Low."),
    "P1309": _("Chassis Acceleration Sensor Signal High."),
    "P1345": _("No SGC Signal (1.6L)."),
    "P1386": _("Knock Sensor Control Zero Test."),
    "P1402": _("EGR Valve Position Sensor Open or Short."),
    "P1449": _("Canister Drain Cut Valve Open or Short (1.8L)."),
    "P1450": _("Excessive Vacuum Leak."),
    "P1455": _("Fuel Tank Sending Unit Open or Short (1.8L)."),
    "P1457": _("Purge Solenoid Valve Low System Malfunction."),
    "P1458": _("A/C Compressor Control Signal Malfunction."),
    "P1485": _("EGR Solenoid Valve Vacuum Open or Short."),
    "P1486": _("EGR Solenoid Valve Vent Open or Short."),
    "P1487": _("EGR Boost Sensor Solenoid Valve Open or Short."),
    "P1496": _("EGR Stepper Motor Malfunction - Circuit 1 (1.8L)."),
    "P1497": _("EGR Stepper Motor Malfunction - Circuit 2 (1.8L)."),
    "P1498": _("EGR Stepper Motor Malfunction - Circuit 3 (1.8L)."),
    "P1499": _("EGR Stepper Motor Malfunction - Circuit 4 (1.8L)."),
    "P1500": _("No Vehicle Speed Signal to TCM."),
    "P1505": _("Idle Air Control Valve Opening Coil Voltage Low."),
    "P1506": _("Idle Air Control Valve Opening Coil Voltage High."),
    "P1507": _("Idle Air Control Valve Closing Coil Voltage Low."),
    "P1508": _("Idle Air Control Valve Closing Coil Voltage High."),
    "P1523": _("VICS Solenoid Valve."),
    "P1586": _("A/T-M/T Codification."),
    "P1608": _("PCM Malfunction."),
    "P1611": _("MIL Request Circuit Voltage Low."),
    "P1614": _("MIL Request Circuit Voltage High."),
    "P1624": _("MIL Request Signal from TCM to ECM."),
    "P1631": _("Alternator ""T"" Open or No Power Output (1.8L)."),
    "P1632": _("Battery Voltage Detection Circuit for Alternator Regulator (1.8L)."),
    "P1633": _("Battery Overcharge."),
    "P1634": _("Alternator ""B"" Open (1.8L)."),
    "P1693": _("MIL Circuit Malfunction."),
    "P1743": _("Torque Converter Clutch Solenoid Valve Open or Short."),
    "P1794": _("Battery or Circuit Failure."),
    "P1795": _("4WD Switch Signal Malfunction."),
    "P1797": _("P or N Range Signal or Clutch Pedal Position Switch Open or Short."),
}
