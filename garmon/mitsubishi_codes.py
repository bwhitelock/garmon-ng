#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# mitsubishi_codes.py
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
    "P1103": _("Turbocharger Wastegate Actuator."),
    "P1104": _("Turbocharger Wastegate Solenoid."),
    "P1105": _("Fuel Pressure Solenoid."),
    "P1300": _("Ignition Timing Adjustment circuit."),
    "P1400": _("Manifold Differential Pressure Sensor circuit."),
    "P1500": _("Alternator FR Terminal circuit."),
    "P1600": _("Serial Communication Link."),
    "P1715": _("Pulse Generator Assembly."),
    "P1750": _("Solenoid Assembly."),
    "P1751": _("A/T Control Relay."),
    "P1791": _("Engine Coolant Temperature Level Input circuit."),
    "P1795": _("Throttle Position Input circuit to TCM."),
}
