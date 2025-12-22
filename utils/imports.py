
from __future__ import division, print_function, annotations
import datetime, time
import logging
import os, sys
import h5py, yaml
from itertools import cycle

import contextlib
from typing import Optional, ClassVar
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.widgets as mwidgets
plt.style.use('utils/style/plotstyle.mplstyle')


import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

from astropy.visualization import quantity_support
import amuse

from amuse.units import units as u, constants as c, nbody_system, quantities
from amuse.units.quantities import AdaptingVectorQuantity
from amuse.lab import  write_set_to_file, read_set_from_file, set_printing_strategy
from amuse_mesa_r2208.interface import Mesa
from amuse.community.ph4.interface import Ph4
from amuse.community.fi.interface import Fi
from amuse.community.phantom.interface import Phantom
from amuse.ext.orbital_elements import generate_binaries
from amuse.ext.star_to_sph import convert_stellar_model_to_sph, pickle_stellar_model
from amuse.ext.sink import new_sink_particles
from amuse.datamodel import Particle, Particles, ParticlesSuperset
from amuse.io.base import IoException
from amuse.couple.bridge import Bridge

from IPython.display import display, HTML
from IPython.core.pylabtools import figsize, getfigs

# import setuptools
from scipy.interpolate import interp1d
import argparse


from collections import Counter


set_printing_strategy(
    "custom",
    preferred_units=[u.MSun, u.RSun, u.s],
    precision=2,
    prefix="",
    separator="",
    suffix=""
)