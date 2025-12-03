
from amuse.lab import  write_set_to_file, read_set_from_file
from amuse.datamodel import  Particle
from amuse.units import units as u, constants as c, nbody_system
from amuse.ext.star_to_sph import  convert_stellar_model_to_sph
from amuse_mesa_r2208.interface import Mesa
from amuse.io.base import IoException


def make_mesa_star(mass_star = 1, N_sph=1000, age=0 , M_core_fraction = 0.2):      # <-- reduce M for speed
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
    
    try:
        sph_star = read_set_from_file(f"./data/setup/star/m={mass_star}N={N_sph}.hdf5")
    except IoException:
        stellar_evolution = Mesa()
        star = Particle(mass=mass_star  | u.MSun, radius=1|u.RSun)
        
        se_star = stellar_evolution.particles.add_particle(star)
        stellar_evolution.commit_particles()
        stellar_evolution.evolve_model(age | u.Myr)                                 # <-- increase age for faster structure convergence
        
        sph_particles = convert_stellar_model_to_sph(
            particle = se_star,
            number_of_sph_particles= N_sph,                             # <-- reduce to 500–1500 for fast runs
            with_core_particle = True,
            target_core_mass = mass_star|u.MSun*M_core_fraction
        )
        stellar_evolution.stop()
        
        sph_particles.gas_particles.name, sph_particles.core_particle.name = "gas","core"
        
        sph_star = sph_particles.gas_particles.copy() 
        sph_star.add_particle(sph_particles.core_particle)
        write_set_to_file(sph_star, f"./data/setup/star/m={mass_star}N={N_sph}.hdf5")
    return sph_star


