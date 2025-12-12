from amuse.lab import *
from utils.imports import *
from utils.binary import get_blackhole_binary
from utils.star import make_mesa_star

def hydro_sink_particles_tramp(sinks, bodies):
    accreted = Particles()
    for s in sinks:
        rsq = s.radius**2
        sx, sy, sz = s.x, s.y, s.z
        
        inside = bodies.select_array(
            lambda x, y, z: (x - sx)**2 + (y - sy)**2 + (z - sz)**2 < rsq,
            ["x","y","z"]
        )
        if len(inside) == 0:
            continue
        
        m_old = s.mass
        m_new = inside.total_mass()

        # update sink
        s.position = (s.position*m_old + inside.center_of_mass()*m_new) / (m_old + m_new)
        s.velocity = (s.velocity*m_old + inside.total_momentum()) / (m_old + m_new)
        s.mass += m_new
        
        accreted.add_particles(inside)
        
    return accreted

def main(rsink, bodies):


    # --- HERE: use your actual binary as sinks ---
    binary = get_blackhole_binary(60, 40)      # your BHs
    binary.radius = rsink                      # give them sink radii
    sinks = binary                             # rename for clarity

    # Run sink accretion
    accreted = hydro_sink_particles_tramp(sinks, bodies)

    print("Accreted particles:", len(accreted))
    for i, s in enumerate(sinks):
        print(f"BH {i}: M={s.mass}, pos={s.position}, vel={s.velocity}")
    return sinks, accreted
    
def new_option_parser():
    from amuse.units.optparse import OptionParser
    result = OptionParser()
    result.add_option("-N", dest="N", type="int",default = 100,
                      help="number of sph particles [100]")
    result.add_option("-M", unit=units.MSun,
                      dest="Mtot", type="float", default = 1|units.MSun,
                      help="Mass of molcular cloud [%default]")
    result.add_option("-R", unit=units.AU,
                      dest="Rvir", type="float", default = 100|units.AU,
                      help="Radius of cloud [%default]")
    result.add_option("-r", unit=units.AU,
                      dest="rsink", type="float", default = 100|units.AU,
                      help="Radius of the sink [%default]")
    return result

if __name__ in ('__main__', '__plot__'):
    o, arguments  = new_option_parser().parse_args()
    main(**o.__dict__)

