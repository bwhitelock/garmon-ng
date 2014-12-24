#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# bmw_codes.py
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
    "P1083": _("Fuel Control Mixture Lean (Bank 1 Sensor 1)"),
    "P1084": _("Fuel Control Mixture Rich (Bank 1 Sensor 1)"),
    "P1085": _("Fuel Control Mixture Lean (Bank 2 Sensor 1)"),
    "P1086": _("Fuel Control Mixture Rich (Bank 2 Sensor 1)"),
    "P1087": _("O2 Sensor Circuit Slow Response in Lean Control Range (Bank 1 Sensor 1)"),
    "P1088": _("O2 Sensor Circuit Slow Response in Rich Control Range (Bank 1 Sensor 1)"),
    "P1089": _("O2 Sensor Circuit Slow Response in Lean Control Range (Bank 1 Sensor 2)"),
    "P1090": _("Pre-Catalyst Fuel Trim Too Lean Bank 1"),
    "P1091": _("Pre-Catalyst Fuel Trim Too Rich Bank 1"),
    "P1092": _("Pre-Catalyst Fuel Trim Too Lean Bank 2"),
    "P1093": _("Pre-Catalyst Fuel Trim Too Rich Bank 2"),
    "P1094": _("O2 Sensor Circuit Slow Response in Rich Control Range (Bank 2 Sensor 1)"),
    "P1095": _("O2 Sensor Circuit Slow Switching From Lean to Rich (Bank 1 Sensor 1)"),
    "P1096": _("O2 Sensor Circuit Slow Switching From Lean to Rich (Bank 2 Sensor 1)"),
    "P1097": _("O2 Sensor Circuit Slow Response after Coast Down Fuel Cutoff (Bank 1 Sensor 1)"),
    "P1098": _("O2 Sensor Circuit Slow Response after Coast Down Fuel Cutoff (Bank 2 Sensor 2)"),
    "P1111": _("Engine Coolant Temperature Radiator Outlet Sensor Low Input"),
    "P1112": _("Engine Coolant Temperature Radiator Outlet Sensor High Input"),
    "P1115": _("Coolant Temperature Sensor Plausibility"),
    "P1116": _("Mass Or Volume Air Flow Circuit Range/Performance Problem (Bank 2)"),
    "P1117": _("Mass Or Volume Air Flow Circuit Low Input (Bank 2)"),
    "P1118": _("Mass Or Volume Air Flow Circuit High Input (Bank 2)"),
    "P1120": _("Pedal Position Sensor Circuit"),
    "P1121": _("Pedal Position 1 Range/Performance Problem"),
    "P1122": _("Pedal Position 1 Low Input"),
    "P1123": _("Pedal Position 1 High Input"),
    "P1132": _("O2 Sensor Heater Control Circuit (Bank 1 Sensor 1)"),
    "P1133": _("O2 Sensor Heater Control Circuit (Bank 2 Sensor 1)"),
    "P1134": _("O2 Sensor Heater Circuit Signal Intermittent (Bank 1 Sensor 2)"),
    "P1135": _("O2 Sensor Heater Circuit Low Voltage (Bank 1 Sensor 1)"),
    "P1136": _("O2 Sensor Heater Circuit High Voltage (Bank 1 Sensor 1)"),
    "P1137": _("O2 Sensor Heater Circuit Signal Intermittant (Bank 1 Sensor 2)"),
    "P1138": _("O2 Sensor Heater Circuit Low Voltage (Bank 1 Sensor 2)"),
    "P1139": _("O2 Sensor Heater Circuit High Voltage (Bank 1 Sensor 2)"),
    "P1140": _("Mass or Volume Air Flow Circuit Range/Performance Problem"),
    "P1145": _("Solenoid Valve Running Losses Control Circuit Electrical"),
    "P1151": _("O2 Sensor Heater Circuit Signal Intermittant (Bank 2 Sensor 1)"),
    "P1152": _("O2 Sensor Heater Circuit Low Voltage (Bank 2 Sensor 1)"),
    "P1153": _("O2 Sensor Heater Circuit High Voltage (Bank 2 Sensor 1)"),
    "P1155": _("O2 Sensor Heater Circuit Intermittant (Bank 2 Sensor 2)"),
    "P1156": _("O2 Sensor Heater Circuit Low Voltage (Bank 2 Sensor 2)"),
    "P1157": _("O2 Sensor Heater Circuit High Voltage (Bank 2 Sensor 2)"),
    "P1158": _("Fuel Trim Additve Bank 1 Low"),
    "P1159": _("Fuel Trim Additve Bank 1 High"),
    "P1160": _("Fuel Trim Additve Bank 2 Low"),
    "P1161": _("Fuel Trim Additve Bank 2 High"),
    "P1162": _("Fuel Trim Additve Per Ignition Bank 1 Low"),
    "P1163": _("Fuel Trim Additve Per Ignition Bank 1 High"),
    "P1164": _("Fuel Trim Additve Per Ignition Bank 2 Low"),
    "P1165": _("Fuel Trim Additve Per Ignition Bank 2 High"),
    "P1174": _("Fuel Trim Adaptation Additve Bank 1 Malfunction"),
    "P1175": _("Fuel Trim Adaptation Additve Bank 2 Malfunction"),
    "P1176": _("O2 Sensor Slow Response Bank 1"),
    "P1177": _("O2 Sensor Slow Response Bank 2"),
    "P1178": _("O2 Sensor Signal Circuit Slow Switching From Rich to Lean (Bank 1 Sensor 1)"),
    "P1179": _("O2 Sensor Signal Circuit Slow Switching From Rich to Lean (Bank 2 Sensor 1)"),
    "P1180": _("O2 Sensor Signal Circuit Slow Switching From Rich to Lean (Bank 1 Sensor 2)"),
    "P1181": _("O2 Sensor Signal Circuit Slow Switching From Rich to Lean (Bank 2 Sensor 2)"),
    "P1182": _("O2 Sensor (Bank 1 Sensor 2) Open Circuit During Coast Down Fuel Cut-off"),
    "P1183": _("O2 Sensor (Bank 2 Sensor 2) Open Circuit During Coast Down Fuel Cut-off"),
    "P1186": _("O2 Sensor Heater Control Circuit (Bank 1 Sensor 2)"),
    "P1187": _("O2 Sensor Heater Control Circuit (Bank 2 Sensor 2)"),
    "P1188": _("Fuel Control (Bank 1 Sensor 1)"),
    "P1189": _("Fuel Control (Bank 2 Sensor 1)"),
    "P1190": _("Pre-catalyst Fuel Trim System Bank 1"),
    "P1191": _("Pre-catalyst Fuel Trim System Bank 2"),
    "P1192": _("Post-catalyst Fuel Trim System Bank 1"),
    "P1193": _("Post-catalyst Fuel Trim System Bank 2"),
    "P1221": _("Pedal Position Sensor 2 Range/Performance Problem"),
    "P1222": _("Pedal Position Sensor 2 Low Input"),
    "P1223": _("Pedal Position Sensor 2 High Input"),
    "P1270": _("Control Module Self-Test, Torque Monitoring"),
    "P1271": _("Ambient Air Pressure Sensor Electrical"),
    "P1283": _("Switching Solenoid for Air Assisted Injection Valves Bank 1 Control Circuit Electrical"),
    "P1284": _("Switching Solenoid for Air Assisted Injection Valves Bank 1 Control Circuit Signal Low"),
    "P1285": _("Switching Solenoid for Air Assisted Injection Valves Bank 1 Control Circuit Signal High"),
    "P1287": _("Switching Solenoid for Air Assisted Injection Valves Bank 2 Control Circuit Electrical"),
    "P1288": _("Switching Solenoid for Air Assisted Injection Valves Bank 2 Control Circuit Signal Low"),
    "P1289": _("Switching Solenoid for Air Assisted Injection Valves Bank 2 Control Circuit Signal High"),
    "P1313": _("'A' Camshaft Position Plausibility"),
    "P1317": _("'B' Camshaft Position Plausibility"),
    "P1327": _("Knock Sensor 2 (Bank 1) Low Input"),
    "P1328": _("Knock Sensor 2 (Bank 1) High Input"),
    "P1332": _("Knock Sensor 4 Low Input"),
    "P1333": _("Knock Sensor 4 High Input"),
    "P1340": _("Multiple Cylinder Misfire During Start"),
    "P1341": _("Multiple Cylinder Misfire With Fuel Cut-off"),
    "P1342": _("Misfire During Start Cylinder 1"),
    "P1343": _("Misfire Cylinder 1 With Fuel Cut-off"),
    "P1344": _("Misfire During Start Cylinder 2"),
    "P1345": _("Misfire Cylinder 2 With Fuel Cut-off"),
    "P1346": _("Misfire During Start Cylinder 3"),
    "P1347": _("Misfire Cylinder 3 With Fuel Cut-off"),
    "P1348": _("Misfire During Start Cylinder 4"),
    "P1349": _("Misfire Cylinder 4 With Fuel Cut-off"),
    "P1350": _("Misfire During Start Cylinder 5"),
    "P1351": _("Misfire Cylinder 5 With Fuel Cut-off"),
    "P1352": _("Misfire During Start Cylinder 6"),
    "P1353": _("Misfire Cylinder 6 With Fuel Cut-off"),
    "P1354": _("Misfire During Start Cylinder 7"),
    "P1355": _("Misfire Cylinder 7 With Fuel Cut-off"),
    "P1356": _("Misfire During Start Cylinder 8"),
    "P1357": _("Misfire Cylinder 8 With Fuel Cut-off"),
    "P1358": _("Misfire During Start Cylinder 9"),
    "P1359": _("Misfire Cylinder 9 With Fuel Cut-off"),
    "P1360": _("Misfire During Start Cylinder 10"),
    "P1361": _("Misfire Cylinder 10 With Fuel Cut-off"),
    "P1362": _("Misfire During Start Cylinder 11"),
    "P1363": _("Misfire Cylinder 11 With Fuel Cut-off"),
    "P1364": _("Misfire During Start Cylinder 12"),
    "P1365": _("Misfire Cylinder 12 With Fuel Cut-off"),
    "P1384": _("Knock Sensor 3 Circuit"),
    "P1385": _("Knock Sensor 4 Circuit"),
    "P1386": _("Control Module Self-test, Knock Control Baseline Test Bank 1"),
    "P1396": _("Crankshaft Position Sensor Segment Timing Plausibility"),
    "P1397": _("Camshaft Position Sensor 'B' Circuit (Bank 1)"),
    "P1400": _("Heated Catalyst Battery Voltage or Current too Low During Heating (Bank 1)"),
    "P1401": _("Heated Catalyst Current too High During Heating (Bank 1)"),
    "P1402": _("Heated Catalyst Power Switch Overtemperature Condition (Bank 1)"),
    "P1403": _("Carbon Canister Shut Off valve Control Circuit Electrical"),
    "P1404": _("Heated Catalyst Current too High During Heating (Bank 2)"),
    "P1405": _("Heated Catalyst Power Switch Overtemperature Condition (Bank 2)"),
    "P1406": _("Heated Catalyst Internal Control Module Checksum/ROM Error"),
    "P1413": _("Secondary Air Injection Pump Relay Control Circuit Signal Low"),
    "P1414": _("Secondary Air Injection System Monitor Circuit High"),
    "P1420": _("Secondary Air Valve Control Circuit Electrical"),
    "P1421": _("Secondary Air System Bank 1"),
    "P1422": _("Secondary Air System Bank 2"),
    "P1432": _("Secondary Air Injection System Incorrect Flow Detected"),
    "P1438": _("Purge Control Valve Control Open Circuit"),
    "P1439": _("Purge Control Valve Control Circuit Signal Low"),
    "P1440": _("Purge Control Valve Control Circuit Signal High"),
    "P1441": _("Leakage Diagnostic Pump Control Open Circuit"),
    "P1442": _("Leakage Diagnostic Pump Control Circuit Signal Low"),
    "P1443": _("Leakage Diagnostic Pump Control Circuit Signal High"),
    "P1444": _("Diagnostic Module Tank Leakage (DM-TL) Pump Control Open Circuit"),
    "P1445": _("Diagnostic Module Tank Leakage (DM-TL) Pump Control Circuit Signal Low"),
    "P1446": _("Diagnostic Module Tank Leakage (DM-TL) Pump Control Circuit Signal High"),
    "P1447": _("Diagnostic Module Tank Leakage (DM-TL) Pump Too High During Switching"),
    "P1448": _("Diagnostic Module Tank Leakage (DM-TL) Pump Too Low During Switching"),
    "P1449": _("Diagnostic Module Tank Leakage (DM-TL) Pump Too High"),
    "P1450": _("Diagnostic Module Tank Leakage (DM-TL) Switching Solenoid Open Circuit"),
    "P1451": _("Diagnostic Module Tank Leakage (DM-TL) Switching Solenoid Control Circuit Signal Low"),
    "P1452": _("Diagnostic Module Tank Leakage (DM-TL) Switching Solenoid Control Circuit Signal High"),
    "P1453": _("Secondary Air Injection Pump Relay Control Circuit Electrical"),
    "P1454": _("Secondary Air Injection Pump With Series Resistor Control Circuit Electrical"),
    "P1456": _("Heated Catalyst Heater Power Supply Open Circuit (Bank 1)"),
    "P1457": _("Heated Catalyst Heater Power Switch Temperature Sensor Electrical (Bank 1)"),
    "P1459": _("Heated Catalyst Heater Power Supply Open Circuit (Bank 2)"),
    "P1460": _("Heated Catalyst Heater Power Switch Temperature Sensor Electrical (Bank 2)"),
    "P1461": _("Heated Catalyst Gate Voltage Signal Low"),
    "P1462": _("Heated Catalyst Internal Control Module Checksum/ROM Error"),
    "P1463": _("Heated Catalyst Battery Temperature Sensor 1 Electrical"),
    "P1464": _("Heated Catalyst Battery Temperature Sensor 2 Electrical"),
    "P1465": _("Heated Catalyst Battery Temperature Sensor 1 or 2 Plausibility"),
    "P1466": _("Heated Catalyst Power Switch Temperature Sensor Plausibility"),
    "P1467": _("Heated Catalyst Comparison Battery Voltages of Power Switches Plausibility"),
    "P1468": _("Heated Catalyst Battery Disconnecting Switch Plausibility"),
    "P1470": _("Leakage Diagnostic Pump Control Circuit Electrical"),
    "P1472": _("Diagnostic Module Tank leakage (DM-TL) Switching Solenoid Control Circuit Electrical"),
    "P1473": _("Diagnostic Module Tank leakage (DM-TL) Pump Current Plausibility"),
    "P1475": _("Leakage Diagnostic Pump Reed Switch Did Not Close"),
    "P1476": _("Leakage Diagnostic Pump Clamped Tube"),
    "P1477": _("Leakage Diagnostic Pump Reed Switch Did Not Open"),
    "P1500": _("Idle Speed Control Valve Stuck Open"),
    "P1501": _("Idle Speed Control Valve Stuck Closed"),
    "P1502": _("Idle Speed Control Valve Closing Solenoid Control Circuit Signal High or Low"),
    "P1503": _("Idle Speed Control Valve Closing Solenoid Control Circuit Signal Low"),
    "P1504": _("Idle Speed Control Valve Closing Solenoid Control Open Circuit"),
    "P1505": _("Idle Speed Control Valve Closing Solenoid Control Circuit Electrial"),
    "P1506": _("Idle Speed Control Valve Open Solenoid Control Circuit Signal High"),
    "P1507": _("Idle Speed Control Valve Open Solenoid Control Circuit Signal Low"),
    "P1508": _("Idle Speed Control Valve Opening Solenoid Control Open Circuit"),
    "P1509": _("Idle Speed Control Valve Opening Solenoid Control Circuit Electrial"),
    "P1510": _("Idle Speed Control Valve Stuck"),
    "P1511": _("DISA Control Circuit Electrical"),
    "P1512": _("DISA Control Circuit Signal Low"),
    "P1513": _("DISA Control Circuit Signal High"),
    "P1519": _("'A' Camshaft Position Actuator Bank 1"),
    "P1520": _("'B' Camshaft Position Actuator Bank 1"),
    "P1522": _("'A' Camshaft Position Actuator Bank 2"),
    "P1523": _("'A' Camshaft Position Actuator Signal Low Bank 1"),
    "P1524": _("'A' Camshaft Position Actuator Signal High Bank 1"),
    "P1525": _("'A' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1526": _("'A' Camshaft Position Actuator Control Open Circuit Bank 2"),
    "P1527": _("'A' Camshaft Position Actuator Control Circuit Signal Low Bank 1"),
    "P1528": _("'A' Camshaft Position Actuator Control Circuit Signal High Bank 1"),
    "P1529": _("'B' Camshaft Position Actuator Control Circuit Signal Low Bank 1"),
    "P1530": _("'B' Camshaft Position Actuator Control Circuit Signal High Bank 1"),
    "P1531": _("'B' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1532": _("'B' Camshaft Position Actuator Control Open Circuit Bank 2"),
    "P1533": _("'B' Camshaft Position Actuator Control Circuit Signal Low Bank 2"),
    "P1534": _("'B' Camshaft Position Actuator Control Circuit Signal High Bank 2"),
    "P1540": _("Pedal Position Sensor"),
    "P1541": _("Pedal Position Sensor Double Error"),
    "P1542": _("Pedal Position Sensor Electrical"),
    "P1543": _("Pedal Position Sensor"),
    "P1544": _("Pedal Position Sensor"),
    "P1545": _("Pedal Position Sensor"),
    "P1546": _("Pedal Position Sensor"),
    "P1550": _("Idle Speed Control valve Closing Solenoid Control Circuit Electrical"),
    "P1551": _("'A' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1552": _("'A' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1556": _("'A' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1560": _("'B' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1564": _("Control Module Selection"),
    "P1565": _("'B' Camshaft Position Actuator Control Open Circuit Bank 1"),
    "P1569": _("'A' Camshaft Position Actuator Control Open Circuit Bank 2"),
    "P1580": _("Throttle Valve Mechanically Stuck"),
    "P1581": _("'B' Camshaft Position Actuator Control Open Circuit Bank 2"),
    "P1589": _("Control Module Self Test, Knock Control Test Pulse Bank 1"),
    "P1593": _("DISA Control Circuit Electrical"),
    "P1594": _("'B' Camshaft Position Actuator Control Open Circuit Bank 2"),
    "P1602": _("Control Module Self Test, Control Module Defective"),
    "P1603": _("Control Module Self Test, Torque Monitoring"),
    "P1604": _("Control Module Self Test, Speed Monitoring"),
    "P1607": _("CAN Version"),
    "P1608": _("Serial Communicating Link Control Module"),
    "P1609": _("Serial Communicating Link EML"),
    "P1611": _("Serial Communicating Link Transmission Control Module"),
    "P1619": _("MAP Cooling Control Circuit Signal Low"),
    "P1620": _("MAP Cooling Control Circuit Signal High"),
    "P1622": _("MAP Cooling Control Circuit Electrical"),
    "P1623": _("Pedal Position Sensor Potentiometer Supply"),
    "P1624": _("Pedal Position Sensor Potentiometer Supply Channel 1 Electrical"),
    "P1625": _("Pedal Position Sensor Potentiometer Supply Channel 2 Electrical"),
    "P1632": _("Throttle Valve Adaptation; Adaptation Condition Not Met"),
    "P1633": _("Throttle Valve Adaptation; Limp Home Position"),
    "P1634": _("Throttle Valve Adaptation; Spring Test Failed"),
    "P1635": _("Throttle Valve Adaptation; Lower Mechanical Stop Not Adapted"),
    "P1636": _("Throttle Valve Control Circuit"),
    "P1637": _("Throttle Valve Position Control; Control Deviation"),
    "P1638": _("Throttle Valve Position Control; Throttle Stuck Temporarily"),
    "P1639": _("Throttle Valve Position Control; Throttle Stuck Permanently"),
    "P1640": _("Internal Control Module (ROM/RAM) Error"),
    "P1690": _("Malfunction Indicator Lamp (MIL) Electrical"),
    "P1734": _("Pressure Control Solenoid 'B' Electrical"),
    "P1738": _("Pressure Control Solenoid 'C' Electrical"),
    "P1743": _("Pressure Control Solenoid 'E' Electrical"),
    "P1744": _("Pressure Control Solenoid 'A' Electrical"),
    "P1746": _("Transmission Control Module Output Stage"),
    "P1747": _("CAN Bus Monitoring"),
    "P1748": _("Transmission Control Module Self Test"),
    "P1749": _("Secondary Pressure Solenoid Communication Error"),
    "P1750": _("Secondary Pressure Solenoid Circuit Range/Performance"),
    "P1751": _("Secondary Pressure Solenoid Open Circuit"),
    "P1761": _("Shift Solenoid Malfunction"),
    "P1765": _("CAN Throttle Valve"),
    "P1770": _("CAN Torque Interface"),
    "P1780": _("CAN Torque Reduction"),
}