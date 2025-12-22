from .imports import *
# =============================================================================
# Config with exploration/science modes
# =============================================================================

DEFAULT_CONFIG = {
    "mode": "science",  # "exploration" or "science"

    # Gravity (Ph4)
    "Ph4": {
        # softer for speed in exploration, smaller for capture/stripping in science         # science default
        "timestep_parameter": 0.14,  # science default
         # keep CPU for determinism unless you need GPU
    },

    # Hydro (Fi)
    "Fi": {
        "use_hydro_flag": True,
        "self_gravity_flag": True,        # can be False for speed; science: True
        "gamma": 5.0/3.0,
        "timestep": 0.0 | u.day,             # science default
        "artificial_viscosity_alpha": 0.5,
        # gravitational softening in hydro; safer epsilon
        "epsilon_squared": (0.01 | u.AU)**2,
    },

    # Bridge (threaded for concurrent kicks)
    "Bridge": {
        "timestep": 0.20 | u.day,     # science default
        "use_threading": True,
    },

    # Evolve
    "evolve": {
        "t_end": 10.0,
        "snapshot_every_day": 5.0,
        "output_dir": "./data/evolution",
        "gravity_file": "gravity_snapshots.hdf5",
        "hydro_file":   "hydro_snapshots.hdf5",
    },

    # Accretion (optional)
    "accretion": {
        "enabled": False,
        "radius_multiplier": 5.0,   # r_acc = multiplier * r_S (or core.radius proxy)
    }
}


# def apply_mode_overrides(cfg: dict) -> dict:
#     cfg = dict(cfg)  # shallow copy
#     mode = cfg.get("mode", "science")

#     if mode == "exploration":
#         cfg["Ph4"]["epsilon_AU"] = 0.08
#         cfg["Ph4"]["timestep_parameter"] = 0.08

#         cfg["Fi"]["self_gravity_flag"] = False
#         cfg["Fi"]["timestep_day"] = 5.0
#         cfg["Fi"]["artificial_viscosity_alpha"] = 1.0

#         cfg["Bridge"]["timestep_day"] = 1.0

#     return cfg

