#!/usr/bin/env python3

# Copyright 2016, 2019 Thomas J. Duck.
# All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Plots field lines for biased dipole."""

from matplotlib import pyplot
import electrostatics
from electrostatics import PointCharge, ElectricField, Potential, GaussianCircle
from electrostatics import finalize_plot

# pylint: disable=invalid-name

XMIN, XMAX = -40, 40
YMIN, YMAX = -30, 30
ZOOM = 6
XOFFSET = 2

electrostatics.init(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET)

# Set up the charges, electric field, and potential.  The point with charge 0
# is a termination point (0 electric field).
charges = [PointCharge(2, [0, 0]),
           PointCharge(-1, [2, 0])]
field = ElectricField(charges)
potential = Potential(charges)

# Set up the Gaussian surfaces
g1 = GaussianCircle(charges[0].x, 29)
g2 = GaussianCircle(charges[1].x, 0.1)

# Create the field lines
fieldlines = []
for x in g1.fluxpoints(field, 12):
    fieldlines.append(field.line(x))
for x in g2.fluxpoints(field, 12):
    fieldlines.append(field.line(x))

# Plotting
pyplot.figure(figsize=(6, 4.5))
field.plot()
potential.plot()
for fieldline in fieldlines:
    fieldline.plot()
for charge in charges:
    charge.plot()
finalize_plot()
pyplot.show()
