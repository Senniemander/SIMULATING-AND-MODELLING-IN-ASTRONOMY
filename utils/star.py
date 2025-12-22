
from amuse.lab import  write_set_to_file, read_set_from_file
from amuse.datamodel import  Particle, ParticlesSuperset
from amuse.units import units as u, constants as c, nbody_system
from amuse.ext.star_to_sph import  convert_stellar_model_to_sph, pickle_stellar_model
from amuse_mesa_r2208.interface import Mesa
from amuse.io.base import IoException
from .imports import *

def evolve_star(mass_star = 1, N_sph=100, age=1 , M_core_fraction = 0.2,):
    
    try: 
        gas = read_set_from_file(f"./data/setup/star/star_n5000.hdf5")
        core_particle_set = read_set_from_file(f"./data/setup/star/core_n1.hdf5")
    except IoException:
        star = Particle(mass=mass_star  | u.MSun, radius = 1|u.RSun)
        stellar_evolution = Mesa()
        star = stellar_evolution.particles.add_particle(star)
        stellar_evolution.evolve_model(age |u.yr)
    
        sph_particles = convert_stellar_model_to_sph(
            particle = star,
            number_of_sph_particles= N_sph, 
            do_store_composition=False,# <-- reduce to 500–1500 for fast runs
            with_core_particle = True,
            target_core_mass = mass_star|u.MSun*M_core_fraction
        )
        gas, core_particle_set = sph_particles.gas_particles, sph_particles.core_particle.as_set()
        gas.velocity  += [0, 200, 0] | u.km/u.s
        stellar_evolution.stop()
        write_set_to_file(gas, f"./data/setup/star/star_n5000.hdf5")
    return gas, core_particle_set

def relax_sph_realization(sph_star, force_update=False):
    
    try: 
        Relax_star = read_set_from_file(f"./data/setup/star/star_Relax_n5000.hdf5")
    except IoException:
        ts_factor = 2.5
        t_end = ts_factor * sph_star.dynamical_timescale(mass_fraction=0.9)
        converter = nbody_system.nbody_to_si(sph_star.dynamical_timescale(), 1|u.RSun)

        hydro = Fi(converter)
        hydro.gas_particles.add_particles(sph_star)
        to_framework = hydro.gas_particles.new_channel_to(sph_star)
        n_steps = ts_factor * 100
        velocity_damp_factor = 1.0 - (ts_factor*2*np.pi)/n_steps
        dt = t_end/float(n_steps)
        time = 0|u.day
        while time < t_end:
            time += dt
            hydro.evolve_model(time)
            hydro.gas_particles.velocity = ( 
                velocity_damp_factor * hydro.gas_particles.velocity
            )
        to_framework.copy()
        hydro.stop()
        write_set_to_file(sph_star, f"./data/setup/star/star_Relax_n5000.hdf5")
    return sph_star