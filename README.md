 # Simulating and Modelling in Astronomy
This repository is part of the Simulating and Modelling in Astronomy course at Leiden University.
The course focuses on developing both computational skills and the ability to model astrophysical phenomena using numerical and physical simulations.

## Project Overview
Our main topic of study is Tidal Disruption Events (TDEs) — events in which a star passes close enough to a black hole to be torn apart by tidal forces.
We aim to model such events in the context of binary black hole systems, exploring how their dynamics affect TDE rates.

## Research Goals
Investigate how two black holes interact without merging.
Determine the critical separation distance between binary black holes that allows them to survive long enough to produce a significant TDE rate.
Study the effects of varying individual black hole masses and how these parameters influence TDE occurrence.
Explore possible extensions, such as clusters of black holes. 
Consider coupling with hydrodynamic simulations using Phantom (SPH code) and bridge methods.

## Tools and Methods
- HermyGrex – for gravitational (ch.4) and hydrodynamic modeling (ch.9)
- Hydro codes – to simulate fluid dynamics (ch.6)
- MESA – stellar evolution modeling
- Phantom (SPH) – smoothed-particle hydrodynamics (ch.6)
- Bridge coupling – combining different simulation domains (ch.9)

## Team Members (Week 15 – 23 Oct)
- Sanne – Lit research, hermygrex, Bridge coupling
- Kelly – Lit research, MESA, Bridge coupling 
- Boyd – Lit research, Phantom (SPH), Bridge coupling

## Research
[Overleaf](https://www.overleaf.com/8617283658fwtpzwswhfwm#dd87c5)

## Star name
options:
- Tramp (lady and the tramp because it gets spaghettified)

This repo is a work in progress but more informartion about the course can be found [here](https://studiegids.universiteitleiden.nl/en/courses/130588/simulation-and-modeling-in-astrophysics-amuse)

## Papers
- Colpi, M. Massive Binary Black Holes in Galactic Nuclei and Their Path to Coalescence. Space Sci Rev 183, 189–221 (2014). https://doi.org/10.1007/s11214-014-0067-1
- Qingjuan Yu, Evolution of massive binary black holes, Monthly Notices of the Royal Astronomical Society, Volume 331, Issue 4, April 2002, Pages 935–958, https://doi.org/10.1046/j.1365-8711.2002.05242.x
- Deborah Mainetti, Alessandro Lupi, Sergio Campana, Monica Colpi, Hydrodynamical simulations of the tidal stripping of binary stars by massive black holes, Monthly Notices of the Royal Astronomical Society, Volume 457, Issue 3, 11 April 2016, Pages 2516–2529, https://doi.org/10.1093/mnras/stw197
- Irrgang, A., Geier, S., Kreuzer, S., Pelisoli, I., & Heber, U. (2020). A stripped helium star in the potential black hole binary LB-1. Astronomy & Astrophysics, 633, L5. https://www.aanda.org/articles/aa/pdf/2020/01/aa37343-19.pdf (really applicable)
- Extreme Tidal Stripping May Explain the Overmassive Black Hole in Leo I: a Proof of Concept
Fabio Pacucci, Yueying Ni, Abraham Loeb https://arxiv.org/pdf/2309.02487

## Requirements 
For 10.000 particles do three runs for three different phases with three different mass ratios

- Movie
- Plot: Mass ratio of the two black holes in the binary on the x-axis vs the fraction of the mass accreted / total mass

