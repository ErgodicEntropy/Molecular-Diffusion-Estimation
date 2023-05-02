# MolecularDynamicsDiffCoeff
Molecular dynamics simulation is a numerical simulation used to study the behavior of molecular systems at the atomic scale. In this project, the goal is to simulate the molecular dynamics of ACN-[BMI][BF4] electrolyte and examine how the diffusion coefficients, energy and volume change in a considered temperature interval. (300K-1200K)

## Introduction:
Molecular dynamics simulation is a numerical simulation used to study the behavior of molecular systems at the atomic scale. This modeling technique makes it possible to predict the physical and chemical properties of these systems by simulating their temporal evolution under the effect of intermolecular forces. In this project, the goal is to simulate the molecular dynamics of ACN-[BMI][BF4] electrolyte and examine how the diffusion coefficients change in a considered temperature interval.
In this document, we will explain in detail the principle of the simulation, the simulation steps by describing them, from the preparation of the initial data to the analysis of the results, then we will identify the indicators used to verify the convergence of the calculation for a simulation of the dynamics analysis of an ACN-[BMI][BF4] electrolyte, as well as a detailed discussion of the results obtained.
## Software used for the simulation:
 -fftool: A python script program used for preparing force field inputs for the construction of the molecular system and the simulation of molecular dynamics.\
 -Packmol: generation program of the studied molecular system (initialization of molecules in a way that prevents the disruptive effects of short-range repulsion forces arising form Pauli's exclusion principle)\
 -VMD: visualization program.\
 -LAMMPS: distribution of programs allowing the simulation of molecular dynamics (OpenMM, CHARMMS, GROMACS, NAMD..etc can be used too)\

## Principles of MD simulation

MD simulation is based on the ''Laplacian'' vision of classical Newtonian mechanics (Laplace's demon thought experiment). It's a computational method used to predict the dynamics of atoms and molecules as they evolve in time. In contrast to statistical mechanics, MD simulation solves the complexity of physical systems (system size; number of particles) by numerically (as opposed to statistically) solving Newton's equations iteratively using Verlet integration, Euler integration (implicit or explicit) or Leapfrog integration...etc.
Because Molecular Dynamics is a simulation, then it's subject to the laws of simulaton. One example is the fact that MD fidelity, speed and numerical stability depend on the simulation components (timestep, timespan, simulation size, simulation box...etc).

## Simulation components:

- Timestep: In MD simulations, the value of the timestep is as crucial as the other simulation components. Usually, the timestep size is of the order of 1 femtosecond ($10^{-15}$ s) as it must be smaller than the period of the fastest vibrating atom/molecule in the system in order to avoid discretization errors.
the timestep size can be increased via SHAKE constraint algorithm which is based on fixing the fastest vibrating atom.
- Timespan: The timespan or total duration of the simulation is the timescale of the simulation and shouldn't be confused with the running time of the simulation though they tend to correlate. The timespan should be large enough in order to be relevant and numerically valid by matching the kinetics of the natural processes. In MD simulations, the timespan is usually of the order of microsecond ($10^{-6}$ s) to nanosecond ($10^{-9}$ s) which is equivalent to CPU-days to CPU-years.
- Simulation Size: In the context of MD simulations, simulation size is the number of particles of the system. Simulation size dictates the computational methods used; explicit or implicit. Naturally, in the case of short systems, explicit methods are preferred while implicit methods (usually those based on mean field theories) are more compatible with large systems.
- Simulation Box: In the context of MD simulations, simulation size is the number of particles of the system. Simulation size dictates the computational methods used; explicit or implicit. Naturally, in the case of short systems, explicit methods are preferred while implicit methods (usually those based on mean field theories) are more compatible with large systems.








