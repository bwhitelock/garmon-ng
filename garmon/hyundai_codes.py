#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# hyundai_codes.py
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
    "P1100": _("Manifold Absolute Pressure (MAP) Sensor Malfunction (Open/Short)"),
    "P1102": _("Manifold Absolute Pressure (MAP) Sensor Malfunction - Low Voltage"),
    "P1103": _("Manifold Absolute Pressure (MAP) Sensor Malfunction - High Voltage"),
    "P1147": _("ETS Sub Accel Position Sensor 1 Malfunction"),
    "P1151": _("ETS Main Accel Position Sensor 2 Malfunction"),
    "P1155": _("ETS Limp Home Valve"),
    "P1159": _("Variable Intake Motor Malfunction"),
    "P1171": _("Electronic Throttle System Open"),
    "P1172": _("Electronic Throttle System Motor Current"),
    "P1173": _("Electronic Throttle System Rationality Malfunction"),
    "P1174": _("Electronic Throttle System #1 Close Malfunction"),
    "P1175": _("Electronic Throttle System #2 Close Malfunction"),
    "P1176": _("ETS Motor Open/Short #1"),
    "P1176": _("ETS Motor Open/Short #2"),
    "P1178": _("ETS Motor Battery Voltage Open"),
    "P1330": _("Spark Timing Adjust Malfunction"),
    "P1521": _("Power Steering Switch Malfunction"),
    "P1607": _("Electronic Throttle System Communication Error"),
    "P1614": _("Electronic Throttle System Module Malfunction"),
    "P1632": _("Traction Control System Malfunction"),
}
