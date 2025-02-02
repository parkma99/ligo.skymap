#
# Copyright (C) 2014-2020  Leo Singer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""Register some extra Matplotlib color maps"""

from importlib import resources

from matplotlib import colormaps
from matplotlib import colors
import numpy as np

__all__ = ()


for name in ['cylon']:
    # Read in color map RGB data.
    with resources.open_text(__package__, name + '.csv') as f:
        data = np.loadtxt(f, delimiter=',')

    # Create color map.
    cmap = colors.LinearSegmentedColormap.from_list(name, data)
    # Assign in module.
    locals().update({name: cmap})
    # Register with Matplotlib.
    colormaps.register(cmap=cmap, force=True)

    # Generate reversed color map.
    name += '_r'
    data = data[::-1]
    cmap = colors.LinearSegmentedColormap.from_list(name, data)
    # Assign in module.
    locals().update({name: cmap})
    # Register with Matplotlib.
    colormaps.register(cmap=cmap, force=True)
