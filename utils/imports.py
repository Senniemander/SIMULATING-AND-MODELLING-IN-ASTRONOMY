
from __future__ import division, print_function
import datetime
import logging
import os
import sys
import time

import h5py
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

import numpy as np
import pandas as pd

import amuse
from amuse.units import units as u, constants as c, nbody_system
from amuse.lab import Hermite, SeBa, Twobody, EVtwin,ph4, Fi, new_powerlaw_mass_distribution, new_powerlaw_mass_distribution_nbody
from amuse_mesa_r2208.interface import Mesa
from amuse.ext.orbital_elements import generate_binaries, orbital_elements, get_orbital_elements_from_binary, new_binary_from_orbital_elements
from amuse.ext.star_to_sph import (pickle_stellar_model, convert_stellar_model_to_SPH, convert_stellar_model_to_sph)

from amuse.ext.solarsystem import get_position
from amuse.ic.plummer import new_plummer_sphere, new_plummer_model
from amuse.ic.gasplummer import new_plummer_gas_model

from amuse.datamodel import Particles, Particle, ParticlesSuperset, Grid
import amuse.io as io
from amuse.couple import bridge

from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs
