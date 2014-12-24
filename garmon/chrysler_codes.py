#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# chrysler_codes.py
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


#from gettext import gettext as _

print "in chrysler"

DTC_CODES_MANUFACTURER = {
    "P1192": _("Inlet Air Temp. Circuit Low"),
    "P1193": _("Inlet Air Temp. Circuit High"),
    "P1195": _("1/1 O2 Sensor Slow During Catalyst Monitor"),
    "P1196": _("2/1 O2 Sensor Slow During Catalyst Monitor"),
    "P1197": _("1/2 O2 Sensor Slow During Catalyst Monitor"),
    "P1198": _("Radiator Temperature Sensor Volts Too High"),
    "P1199": _("Radiator Temperature Sensor Volts Too Low"),
    "P1281": _("Engine Is Cold Too Long"),
    "P1282": _("Fuel Pump Relay Control Circuit"),
    "P1283": _("Idle Select Signal Invalid"),
    "P1284": _("Fuel Injection Pump Battery Voltage Out Of Range"),
    "P1285": _("Fuel Injection Pump Controller Always On"),
    "P1286": _("Accelerator Pedal Position Sensor Supply Voltage Too High"),
    "P1287": _("Fuel Injection Pump Controller Supply Voltage Low"),
    "P1288": _("Intake Manifold Short Runner Solenoid Circuit"),
    "P1289": _("Manifold Tune Valve Solenoid Circuit"),
    "P1290": _("CNG Fuel Pressure Too High"),
    "P1291": _("No Temp Rise Seen From Fuel Heaters"),
    "P1292": _("CNG Pressure Sensor Voltage Too High"),
    "P1293": _("CNG Pressure Sensor Voltage Too Low"),
    "P1294": _("Target Idle Not Reached"),
    "P1295": _("No 5 Volts To TP Sensor"),
    "P1296": _("No 5 Volts To MAP Sensor"),
    "P1297": _("No Change in MAP From Start To Run"),
    "P1298": _("Lean Operation At wide Open Throttle"),
    "P1299": _("Vacuum Leak Found (IAC Fully Seated)"),
    "P1388": _("Auto Shutdown (ASD) Relay Control Circuit"),
    "P1389": _("No Auto Shutdown (ASD) Relay Output Voltage At PCM"),
    "P1390": _("Timing Belt Skipped One Tooth or More"),
    "P1391": _("Intermittent Loss of CMP or CKP"),
    "P1398": _("Mis-Fire Adapter Numerator at Limit"),
    "P1399": _("Wait To Start Lamp Circuit"),
    "P1403": _("No 5 Volts To EGR Sensor"),
    "P1475": _("Aux. 5 Volt Output Too High"),
    "P1476": _("Too Little Secondary Air"),
    "P1477": _("Too Much Secondary Air"),
    "P1478": _("Battery Temp Sensor Volts Out of Limit"),
    "P1479": _("Transmission Fan Relay Circuit"),
    "P1480": _("PCV Solenoid Valve"),
    "P1482": _("Catalyst Temperature Sensor Circuit Shorted Low"),
    "P1483": _("Catalyst Temperature Sensor Circuit Shorted High"),
    "P1484": _("Catalytic Converter Overheat Detected"),
    "P1485": _("Air Injection Solenoid Circuit"),
    "P1486": _("Evap Leak Monitor Pinched Hose"),
    "P1487": _("Hi Speed Rad Fan CTRL Relay Circuit"),
    "P1488": _("Auxiliary 5 Volt Supply Output Too Low"),
    "P1489": _("High Speed Fan CTRL Relay Circuit"),
    "P1490": _("Low Speed Fan CTRL Relay Circuit"),
    "P1491": _("Rad Fan Control Relay Circuit"),
    "P1492": _("Battery Temperature Sensor Voltage Too High"),
    "P1493": _("Battery Temperature Sensor Voltage Too Low"),
    "P1494": _("Leak Detection Pump Switch or Mechanical Fault"),
    "P1495": _("Leak Detection Pump Solenoid Circuit"),
    "P1496": _("5 Volt Supply Output Too Low"),
    "P1498": _("High speed Rad Fan Ground CTRL Rly Circuit"),
    "P1594": _("Charging System Voltage Too High"),
    "P1595": _("Speed Control Solenoid Circuits"),
    "P1596": _("Speed Control Switch Always High"),
    "P1597": _("Speed Control Switch Always Low"),
    "P1598": _("A/C Pressure Sensor Volts Too High"),
    "P1599": _("A/C Pressure Sensor Volts Too Low"),
    "P1602": _("PCM Not Programmed"),
    "P1680": _("Clutch Released Switch Circuit"),
    "P1681": _("No I/P Cluster CCD/J1850 Messages Received"),
    "P1682": _("Charging System Voltage Too Low"),
    "P1683": _("Speed Control Power Relay Or Speed Control 12 Volt Driver Circuit"),
    "P1684": _("Battery Disconnected Within Last 50 Starts"),
    "P1685": _("Skim Invalid Key"),
    "P1686": _("No SKIM Bus Message Received"),
    "P1687": _("No Cluster Bus Message"),
    "P1688": _("Internal Fuel Injection Pump Controller Failure"),
    "P1689": _("No Communication Between ECM & Injection Pump Module"),
    "P1690": _("Fuel injection pump CKP Sensor Does Not Agree With ECM CKP Sensor"),
    "P1691": _("Fuel Injection Pump Controller Calibration Failure"),
    "P1693": _("DTC Detected In ECM Or PCM"),
    "P1694": _("No CCD Messages Received From ECM"),
    "P1695": _("No CCD/J185O Message From BCM"),
    "P1696": _("PCM Failure EEPROM Write Denied"),
    "P1697": _("PCM Failure SRI Mile Not Stored"),
    "P1698": _("No CCD Messages Received From PCM"),
    "P1719": _("Skip Shift Solenoid Circuit"),
    "P1740": _("TCC Or OD Solenoid Performance"),
    "P1756": _("Governor Pressure Not Equal To Target At 15�20 PSI"),
    "P1757": _("Governor Pressure Above 3 PSI When Request Is 0 PSI"),
    "P1762": _("Governor Pressure Sensor Offset Improper Voltage"),
    "P1763": _("Governor Pressure Sensor Voltage Too High"),
    "P1764": _("Governor Pressure Sensor Voltage Too Low"),
    "P1765": _("Trans 12 Volt Supply Relay Control Circuit"),
    "P1899": _("Park/Neutral Position Switch Stuck In Park or In Gear"),
}
