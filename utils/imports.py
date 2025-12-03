
from __future__ import division, print_function
import datetime
import logging
import os
import sys
import time

import h5py


import amuse

from amuse.units import units as u, constants as c, nbody_system
from amuse.lab import  write_set_to_file, read_set_from_file, set_printing_strategy

from amuse_mesa_r2208.interface import Mesa
from amuse.community.ph4 import Ph4
from amuse.community.fi import Fi

from amuse.ext.orbital_elements import generate_binaries
from amuse.ext.star_to_sph import convert_stellar_model_to_sph

from amuse.datamodel import Particle, Particles
from amuse.io.base import IoException
from amuse.couple.bridge import Bridge

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs

# set_printing_strategy(
#     "custom",
#     preferred_units=[u.MSun, u.RSun, u.Myr],
#     precision=6,
#     prefix="",
#     separator="[",
#     suffix="]"
# )