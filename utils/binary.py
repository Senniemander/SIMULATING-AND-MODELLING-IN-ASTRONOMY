from amuse.lab import *
from amuse.ext.orbital_elements import generate_binaries
from amuse.io.base import IoException
from amuse.lab import write_set_to_file, read_set_from_file
from .imports import *

def get_blackhole_binary(m1:int, m2:int, a_bbh = 1, e_bbh = 0):
    """
    Create a tuple of particles for the black holes using the passed
    parameters, then add those particles to the Particles class
    and lastly move the center of mass to the origin
    
    Larger masses m1 and/or m2 will increase the duration of the runs
    
    The same goes for larger separations a
    """
    try:
        binary = read_set_from_file(f"./data/setup/binary/m1={m1}m2={m2}a={a_bbh}e={e_bbh}.hdf5")
    except IoException:
        bh1, bh2 = generate_binaries(
            m1 | u.MSun, 
            m2 | u.MSun, 
            a_bbh | u.AU, 
            e_bbh,              # unitless
            G = constants.G
            )
        bh1.name, bh2.name = "primary", "secondary"
        rs = lambda m: 2*c.G*m/c.c**2
        bh1.radius, bh2.radius = rs(bh1.mass), rs(bh2.mass)
        binary = Particles()
        binary.add_particle(bh1), binary.add_particle(bh2)
        binary.move_to_center()
        write_set_to_file(binary, f"./data/setup/binary/m1={m1}m2={m2}a={a_bbh}e={e_bbh}.hdf5")
    return binary