
from amuse.lab import  write_set_to_file, read_set_from_file
from amuse.datamodel import  Particle, ParticlesSuperset
from amuse.units import units as u, constants as c, nbody_system
from amuse.ext.star_to_sph import  convert_stellar_model_to_sph, pickle_stellar_model
from amuse_mesa_r2208.interface import Mesa
from amuse.io.base import IoException
from .imports import *

def evolve_star(mass_star = 1, N_sph=100, age=1 , M_core_fraction = 0.2,):
    """
    Initializing a star using Mesa and converting the stellar model into sph
    
    To significantly speed up the code, try first to read the set of the given combination
    of parameters from the corresponding file. If no such file exists yet, we initialize a new instance 
    with the given parameters and then proceed to write it to a file for future reference
        Parameters:
            mass_star (float): value of the mass of the star in Msun
            N_sph (int): Number of particles
            age (float): value of the age in Myr
            M_core_fraction (float): The fraction of the mass of the star that is contained in the core
        Returns: 
            sph_star (Particles): particle set wiht both the gas particles and the core particle
   """
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
    gas, core = sph_particles.gas_particles, sph_particles.core_particle.as_set()
    gas.velocity  += [0, 200, 0] | u.km/u.s
    stellar_evolution.stop()
    return gas, core

def relax_sph_realization(sph_star, force_update=False):
    # sph_star = read_set_from_file(filename)['gas']
    ts_factor = 2.5
    t_end = ts_factor * sph_star.dynamical_timescale(mass_fraction=0.8)
    filename= f"./data/setup/star/relaxed_{t_end}.hdf5"

    dynamical_timescale = sph_star.dynamical_timescale()
    converter = nbody_system.nbody_to_si(1|u.MSun, 1|u.RSun)
    
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
        hydro.gas_particles.velocity = velocity_damp_factor * hydro.gas_particles.velocity
        to_framework.copy()
        sph_star.savepoint(timestamp=hydro.model_time)
    
    hydro.stop()
    return sph_star




# from amuse.lab import  write_set_to_file, read_set_from_file
# from amuse.datamodel import  Particle, ParticlesSuperset
# from amuse.units import units as u, constants as c, nbody_system
# from amuse.ext.star_to_sph import  convert_stellar_model_to_sph, pickle_stellar_model
# from amuse_mesa_r2208.interface import Mesa
# from amuse.io.base import IoException
# from .imports import *

# def evolve_star():
# def relax_sph_realization(sph_star, force_update=False):
#     # sph_star = read_set_from_file(filename)['gas']
#     ts_factor = 2.5
#     t_end = ts_factor * sph_star.dynamical_timescale(mass_fraction=0.8)
#     filename= f"./data/setup/star/relaxed_{t_end}.hdf5"
#     try:
#         relaxed = read_set_from_file(filename)
#     except IoException:
#         dynamical_timescale = sph_star.dynamical_timescale()
#         converter = nbody_system.nbody_to_si(1|u.MSun, 1|u.RSun)
        
#         hydro = Fi(converter)
#         hydro.gas_particles.add_particles(sph_star)

#         to_hydro = sph_star.new_channel_to(hydro.gas_particles)
#         to_framework = hydro.gas_particles.new_channel_to(sph_star)

        
#         n_steps = ts_factor * 100
#         velocity_damp_factor = 1.0 - (ts_factor*2*np.pi)/n_steps
#         dt = t_end/float(n_steps)
#         time = 0|u.day
#         write_set_to_file(sph_star.savepoint(hydro.model_time), 
#                                 ,
#                                 overwrite_file = True,)
#         while time < t_end:
#             time += dt
#             hydro.evolve_model(time)
#             hydro.gas_particles.velocity = velocity_damp_factor * hydro.gas_particles.velocity
#             to_framework.copy()
#             write_set_to_file(sph_star.savepoint(hydro.model_time), 
#                                 f"./data/setup/star/relaxed_{t_end}.hdf5",
#                                 append_to_file = True
#                                 )
            
#         hydro.stop()
#     return sph_star

# def make_mesa_star(mass_star = 1, N_sph=100, age=1 , M_core_fraction = 0.2, overwrite=False):      # <-- reduce M for speed
#     """
#     Initializing a star using Mesa and converting the stellar model into sph
    
#     To significantly speed up the code, try first to read the set of the given combination
#     of parameters from the corresponding file. If no such file exists yet, we initialize a new instance 
#     with the given parameters and then proceed to write it to a file for future reference
#         Parameters:
#             mass_star (float): value of the mass of the star in Msun
#             N_sph (int): Number of particles
#             age (float): value of the age in Myr
#             M_core_fraction (float): The fraction of the mass of the star that is contained in the core
#         Returns: 
#             sph_star (Particles): particle set wiht both the gas particles and the core particle
   
#     """
#     filename = f"./data/setup/star/m={mass_star}N={N_sph}age={age}.hdf5"
#     try:
#         gas, core = read_set_from_file(filename, names=["gas","core"])
#     except IoException:
#         stellar_evolution = Mesa()
#         star = Particle(mass=mass_star  | u.MSun, radius = 1|u.RSun)
        
#         stellar_evolution.particles.add_particle(star)
#         stellar_evolution.commit_particles()
#         # stellar_evolution.evolve_model(age | u.yr)                                 # <-- increase age for faster structure convergence
#         # to_framework = stellar_evolution.particles.new_channel_to(star)
        
#         while stellar_evolution.model_time < age |u.yr:
#             stellar_evolution.evolve_model()
        
#         sph_particles = convert_stellar_model_to_sph(
#             particle = stellar_evolution.particles[0],
#             number_of_sph_particles= N_sph, 
#             do_store_composition=False,# <-- reduce to 500–1500 for fast runs
#             with_core_particle = True,
#             target_core_mass = mass_star|u.MSun*M_core_fraction
#         )
        
#         gas, core = sph_particles.gas_particles, sph_particles.core_particle.as_set()
#         gas.velocity  += [0, 20, 0] | u.km/u.s
#         # core.velocity  += [0, 20, 0] | u.km/u.s
#         write_set_to_file([gas, core], 
#                             filename,
#                             names=["gas","core"],
#                             overwrite_file = True)
#         stellar_evolution.stop()
#     # gas_relaxed = relax_sph_realization(gas.copy())
#     return gas, core


