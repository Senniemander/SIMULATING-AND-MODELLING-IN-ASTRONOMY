
from amuse.lab import units, write_set_to_file, read_set_from_file
from amuse.datamodel import Particles, Particle, ParticlesSuperset, Grid
from amuse.ext.orbital_elements import generate_binaries
from amuse.ext.star_to_sph import convert_stellar_model_to_SPH, convert_stellar_model_to_sph
from amuse_mesa_r2208.interface import Mesa
from amuse.io.base import IoException
# ============================================================
# 1) Build a MESA star
# ============================================================
def make_mesa_star(mass_star = 1 | units.MSun, N_sph=1000, age=0 | units.Myr, M_core_fraction = 0.2):      # <-- reduce M for speed
    try:
        sph_star = read_set_from_file(f"./data/setup/star/m={mass_star}N={N_sph}")
    except IoException:
        star = Particle(mass=mass_star)
        stellar_evolution = Mesa()
        se_star = stellar_evolution.particles.add_particle(star)
        stellar_evolution.commit_particles()
        stellar_evolution.evolve_model(age)                                 # <-- increase age for faster structure convergence
        sph_particles = convert_stellar_model_to_sph(
            particle = se_star,
            number_of_sph_particles= N_sph,                             # <-- reduce to 500–1500 for fast runs
            with_core_particle = True,
            target_core_mass = mass_star*M_core_fraction
        )
        stellar_evolution.stop()
        
        sph_particles.gas_particles.name = "gas"
        sph_particles.core_particle.name = "core"
        
        sph_star = sph_particles.gas_particles.copy()
        sph_star.add_particle(sph_particles.core_particle)
        write_set_to_file(sph_star, f"./data/setup/star/m={mass_star}N={N_sph}" )
    return sph_star


