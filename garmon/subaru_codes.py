#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# subaru_codes.py
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
    "P1086": _("Tumble generator valve #2 (LH) position sensor circuit low input"),
    "P1087": _("Tumble generator valve #2 (LH) position sensor circuit high input"),
    "P1088": _("Tumble generator valve #1 (RH) position sensor circuit low input"),
    "P1089": _("Tumble generator valve #1 (RH) position sensor circuit high input"),
    "P1090": _("Tumble generator valve #1 (RH) malfunction (stuck open)"),
    "P1091": _("Tumble generator valve #1 (RH) malfunction (stuck close)"),
    "P1092": _("Tumble generator valve #2 (LH) malfunction (stuck open)"),
    "P1093": _("Tumble generator valve #2 (LH) malfunction (stuck close)"),
    "P1094": _("Tumble generator valve circuit #1 (open circuit)"),
    "P1095": _("Tumble generator valve circuit #1 (over current)"),
    "P1096": _("Tumble generator valve circuit #2 (open circuit)"),
    "P1097": _("Tumble generator valve circuit #2 (over current)"),
    "P1100": _("Starter Switch Circuit Malfunction"),
    "P1101": _("Neutral Position Switch Circuit High Input (A/T)"),
    "P1101": _("Neutral Position Switch Circuit Malfunction (M/T)"),
    "P1102": _("Pressure Sources Solenoid Valve Circuit Malfunction"),
    "P1103": _("Pressure Sources Switching Solenoid Valve Circuit"),
    "P1104": _("Engine Torque Control Signal Circuit Malfunction"),
    "P1106": _("Engine Torque Control Signal 2 Circuit Malfunction"),
    "P1110": _("Atmospheric pressure sensor low input"),
    "P1111": _("Atmospheric pressure sensor high input"),
    "P1112": _("Atmospheric pressure sensor range/performance problem"),
    "P1115": _("Engine Torque Control Cut Signal Circuit High Input"),
    "P1116": _("Engine Torque Control Cut Signal Circuit Low Input"),
    "P1120": _("Starter Switch High Input"),
    "P1121": _("Neutral Position Switch Circuit High Input [MT Vehicles]"),
    "P1121": _("Neutral Position Switch Circuit Low Input [AT Vehicles]"),
    "P1122": _("Pressure Sources Switching Valve Circuit High Input"),
    "P1124": _("TCS Signal Circuit High Input"),
    "P1130": _("Front oxygen sensor circuit malfunction (open circuit)"),
    "P1131": _("Front oxygen sensor circuit malfunction (short circuit)"),
    "P1134": _("Front oxygen (A/F) sensor microcomputer problem"),
    "P1135": _("Front Left Oxygen Sensor Circuit Open"),
    "P1136": _("Front Left Oxygen Sensor Curcuit Shorted"),
    "P1137": _("Front oxygen (A/F) sensor circuit range/performance problem"),
    "P1139": _("Front oxygen (A/F) sensor #1 heater circuit performance/range problem"),
    "P1140": _("Front Left Oxygen Sensor Heater Circuit Range"),
    "P1141": _("Mass Air Flow Sensor Circuit High Input"),
    "P1142": _("Mass Air Flow Sensor Circuit Low Input"),
    "P1143": _("Pressure Sensor Circuit Low Input"),
    "P1144": _("Pressure Sensor Circuit High Input"),
    "P1146": _("Pressure sensor circuit range/performance problem (high input)"),
    "P1150": _("Front Oxygen Sensor Heater Circuit High Input"),
    "P1151": _("Rear Oxygen Sensor Heater Circuit High Input"),
    "P1230": _("Fuel pump control unit malfunction"),
    "P1244": _("Wastegate control solenoid valve malfunction (low input)"),
    "P1245": _("Wastegate control solenoid valve malfunction (fail-safe)"),
    "P1301": _("Fire due to increased exhaust temperature"),
    "P1312": _("Exhaust temperature sensor malfunction"),
    "P1325": _("Knock Sensor Circuit Low Input"),
    "P1400": _("Fuel Tank Pressure Control Solenoid Low Input"),
    "P1420": _("Fuel Tank Pressure Control Solenoid High Input"),
    "P1421": _("Exhaust Gas Recirculation Circuit High Input"),
    "P1422": _("EVAP Purge Control Valve Circuit High Input"),
    "P1423": _("EVAP Vent Control High Input"),
    "P1440": _("Fuel Tank Pressure Control System Low Input"),
    "P1441": _("Fuel Tank Pressure Control System High Input"),
    "P1442": _("Fuel Level Sensor Circuit Range/Perf"),
    "P1443": _("EVAP Control System Vent Control Function Problem"),
    "P1480": _("Cooling fan relay 1 circuit high input"),
    "P1500": _("Radiator Fan Relay 1 Circuit Malfunction"),
    "P1501": _("Idle Control System Malfunction (Fail Safe)"),
    "P1502": _("Radiator Fan Function Problem"),
    "P1507": _("Idle Control System Malfunction (Fail Safe)"),
    "P1510": _("Idle Air Control Solenoid Signal 1 Circuit Low Input"),
    "P1511": _("Idle Air Control Solenoid Signal 1 Circuit High Input"),
    "P1512": _("Idle Air Control Solenoid Signal 2 Circuit Low Input"),
    "P1513": _("Idle Air Control Solenoid Signal 2 Circuit High Input"),
    "P1514": _("Idle Air Control Solenoid Signal 3 Circuit Low Input"),
    "P1515": _("Idle Air Control Solenoid Signal 3 Circuit High Input"),
    "P1516": _("Idle Air Control Solenoid Signal 4 Circuit Low Input"),
    "P1517": _("Idle Air Control Solenoid Signal 4 Circuit High Input"),
    "P1518": _("Starter switch circuit low input"),
    "P1520": _("Radiator Fan Relay 1 Circuit High Input"),
    "P1540": _("Vehicle Speed Sensor Malfunction 2"),
    "P1544": _("High exhaust temperature detected"),
    "P1560": _("Back-Up Voltage Circuit Malfunction"),
    "P1590": _("Neutral position switch circuit high input"),
    "P1591": _("Neutral position switch circuit low input"),
    "P1592": _("Neutral position switch circuit (MT model)"),
    "P1594": _("Automatic transmission diagnosis input signal circuit malfunction"),
    "P1595": _("Automatic transmission diagnosis input signal circuit low input"),
    "P1596": _("Automatic transmission diagnosis input signal circuit high input"),
    "P1698": _("Engine torque control cut signal circuit low input"),
    "P1699": _("Engine torque control cut signal circuit high input"),
    "P1700": _("Throttle Position Sensor Circuit Malfunction (A/T)"),
    "P1701": _("Cruise Control Set Signal Circuit Malfunction (A/T)"),
    "P1702": _("Auto Trans Diagnosis Input Signal Circuit"),
    "P1703": _("Low clutch timing control solenoid valve circuit malfunction"),
    "P1704": _("2-4 Brake Timing Solenoid Valve Circuit Malfunction"),
    "P1705": _("2-4 Brake Pressure Solenoid Valve (Solenoid D) Circuit"),
    "P1711": _("Engine torque control signal 1 circuit malfunction"),
    "P1712": _("Engine torque control signal 2 circuit malfunction"),
    "P1722": _("Auto Trans Diagnosis Input Signal High Input"),
    "P1742": _("Auto Trans Diagnosis Input Signal Malfunction"),
}
