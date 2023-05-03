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

## Simulation steps: 

-Initialization: it can be random Gaussians for velocities and/or coordinates. This process might be followed by ''packing'' all atoms in one corner (thanks to Packmol software) to avoid perturbation that may result from short-range repulsions (Pauli exclusion principle).
- Potential Evaluation: This is the most CPU intensive step due to the evaluation of non-bonded (pairstyle) potential ie; Couloumb potential and Van Der Wals force. This is due to the fact that although intermolecular forces are weaker than intramolecular forces (which is the reason why we have molecules), intermolecular forces are non local which implies that their influence pervades all the system (worst-case scenario of a complexity of O(n^{2})).
- Energy minimization/equilibration: Energy equilibration is rendering kinetic energy equally distributed among constituent particles (this can be done using methods like dynamically-updated velocity rescaling). Energy minimization is the process of relaxing the system to its stable state in order to render the simulation more accurate and more representative of reality
- LAMMPS run: Predict the motion by updating the values of coordinates and velocities by integrating Newton's equations (this is basically what LAMMPS ''run'' commands does)
- Data collection: This is the step after the simulation terminates, collecting average values of parameters of interest (diffusion, temperature..etc)
- Data analysis: This is a very important step (contrary to popular believes) because it's the step where one has to analyze the average values obtained from the simulation to see whether the simulation is accurate, converges or stable. If the simulation is fine, then it's a good opportunity to virtually investigate the system accurately without the need to experimentations (in the case of experiments being dangerous, time consuming or merely impossible). Data analysis is the step where it is possible to infer conclusions about atom-level phenomena that are not directly observed or purely virtual (alternative events that didn't happen in the physical world..etc)

## Diffusion coefficient: 

Diffusion is the irreversible phenomenon of particles movement en mass from region of high concentration to reigions with low concentration following Fick's law.

Fick's first law is a phenomenological law (just like its counterpart Fourier's law) meaning that it's not derived from theory nor it's universal, but it's derived from observation in a way that's nonetheless coherent with theory. Fick's first law indicates the relationship between the diffusion flux and concentration gradient as follow:
J = -D * (∂φ/∂x)








Fick's first law is a form of a moderation law (in the sense of control theory) because it's a regulation of a perturbation (the gradient of the concentration ie; the heterogeneity of concentration in space)

Fick's second law, just like the first law, is describing the same phenomenon but in a way that provides a fundamental insight about the phenomenon of diffusion; namely its relationship with the second law of thermodynamics. Fick's second law is stated as follow:

(∂φ/∂t) = D * (∂^2φ/∂x^2)






Fick's second law is similar to the heat equation. Both are characterized by a time-reversal asymmetry (unlike D'alembert wave propagation equation) because of the first derivative with respect to time which indicates the irreversible nature of the diffusion phenomenon. Such a time-reversal asymmetry is due to the second law of thermodynamics which states that in closed systems, entropy never decreases and only increases (thus engendering the arrow of time; a hypothesis under the name of thermal time hypothesis put forth by Carlo Rovelli and Alain Connes)
Given the time-reversal asymmetric nature of diffusion equation, it's said not to conserver information. This is known as Noether's theorem (symmetries in physics always correspond to a certain law of conservation; in the case of time-reversal symmetry, it's the information in the sense of Shannon)

From the point of view of simulation and mathematical modeling, diffusion can be modeled using random walks or Levy flights or Markov chains with the assumption of ergodicity. Because diffusion is a form of homogenization (recall the moderation law) therefore it's by definition an ergodic phenomenon (the second law of thermodynamics is a physical reformulation of the ergodic hypothesis first put forth by Ludwig Boltzmann)

## Discussion of results: 

The results of the simulation indicate that the total energy, diffusion coefficient and volume increase with temperature. The following figures are illustrative representations of the results of the simulation:







For the diffusion coefficient, the simulation results match the reality in encapsulating the relationship between diffusion coefficient and temperature. To recall, Einstein's relation (Stokes-Einstein-Smoluchowski equation) states that diffusion coefficient D is proportional to temperature T with the proportionality constant being the particles mobility (intrinsic to the molecules) times Boltzmann constant:

D = μ * k_B * T


Albeit neglecting quantum effects playing out at the level of hydrogen bonds thanks to the Born-Oppenheimer approximation, we still managed to get results that reflect empirical reality. Therefore, this is an indication that the simulation is of high-fidelity which in turns implies that the model used (Newtonian dynamics) is accurate and representative of microscopic phenomena up to a certain threshold (dictated by the complementarity principle of Niels Bohr) beyond which the B-O approximation breaks down.\
On a more fundamental level, the results of the simulation, guaranteeing high fidelity, reflect something deeper about the nature of the universe captured by one of the most famous concepts in statistical mechanics which is the fluctuation-dissipation theorem which is a phenomenological result from the field of statistical physics that is ''fundamental'' meaning that it occurs in different areas of physics (light absorption-heat, Johnson noise-Resistors, Diffusion-Joule Energy) due to the fact that it doesn't assume any natural laws (black-box) about the system it studies, resulting only from the a purely mathematical (statistical, to be precise) examination of the system. The theorem states that at equilibrium, any system in a detailed balance (stationary distribution of reversible Markov chain) such that for each elementary process there exists a reverse process that balances it, a process that causes energy dissipation (captured by abstracting the notion of impedance or admittance from electricity) by turning it into heat, is balanced by a reverse process in the form of thermal fluctuation which converts that heat back to the original form of energy (usually, kinetic energy).\
In our example, incorporating solvent effects and using ''fix viscous'' LAMMPS command to fix the damp factor value (= 100), that caused the particles to dissipate their kinetic energy due to friction and viscosity, that in turn led to thermal fluctuations manifested in an increasing kinetic energy (Brownian motion) captured by an increasing diffusion coefficient.\


## Interesting applications of MD simulation in Optimization theory and Operations Research:
### Demon algorithm:
This is a Monte Carlo method (or a metaheuristic to be more precise) used to ''solve'' the system in non-equilibrium statistical mechanics or when the system size is too large (a lot of number of particles) to the point where brute-force exhaustive (explicit) search becomes computationally expensive\
The method assumes ergodicity (or at least quasi-ergodicity) for efficiently sampling from the microcanonical ensemble NVE with an additional degree of freedom called ''demon'' (intended here to be the reversed version of Maxwell's demon) that exchanges energy with the system to reach equilibrium while maintaining constant energy (energy conservation) without interacting with particles.\
This method is inspired from MD simulations in the attempt to solve the system implicitly (more precisely, stochastically) instead of expensive calculations of velocity and position for every particle, by defining the microscopic variables that are consistent with macroscopic variables (note that there are many microstate configurations that can result in the same macrostate thus the complexity of the problem; Multiple realizability)\
The point of the algorithm is to lower the potential energy E in order to reach thermodynamic equilibrium while conserving total energy by storing lost E values in the demon energy Ed. In optimization problems, the potential energy E is the function we want to minimize. Aside from conserving total energy, Ed Demon's energy plays the role of an exploration catalyzer/tolerance, the greater its value the more incentive/tendency there is to explore the search space. For instance, dE < 0 = exploitation phase. Also, the thing about the Demon algorithm is that the exploitation-exploration trade-off is balanced via a feedback loop via having exploiting a solution adds up to Ed. Demon algorithm can be used to optimize non-linear functions with multimodal features. 
### Particle Swarm Optimization:
This metaheuristic is based on the notion of swarm intelligence defined as the collectively emergent behavior of a decentralized, self-organized system (swarm) of agents following simple rules (position, velocity) interacting with each others until a global intelligence behavior emerge (similar to individual-based models). Examples include: Ant colonies, Bee colonies, bird flock, fish schooling, social behavior...etc.\
The idea behind PSO is simple; implementing a hybrid (collective and individual) exploration where individual agents (particles) move according to simple rules dictated by a relation between position and velocity (Verlet integration) guided by a local best-known position in the search space and the global best-known position for the whole system that are discovered. The next step is to perform a movement en mass towards one of those position (depending on strength of social coefficient vs cognitive coefficient)\
PSO is efficient at balancing between exploration and exploitation manifested in the value of vi,max for each particle (or vmax for all particles) such that high vmax encourages exploration and low vmax encourages exploitation of the path found to the solution. Of course, an adaptive strategy has to be performed in order to come up with the efficient value of vmax depending on the nature of the system (number of particles initialized, social/cognitive coefficients...etc)\
There is a similarity between this metaheuristic and molecular dynamics simulation because they can be expressed in almost the same notions (particles, positions, velocities, energy minimization...etc) thus they are structurally the same implying that MD simulation can indeed be used to solve optimization problems involving non-linear, multimodal or non-convex objective functions\
We wrote a modified version of PSO that is related to statistical physics (and thus to MD simulations) based on Maxwell-Boltzmann distribution instead of uniform or normal distribution for sampling velocities in the algorithm (original version) and it yielded the same results as the original which reflect physical reality (M-B distribution of velocity).

## Conclusion:
In conclusion, the temperature study of the diffusion phenomenon in the ACN-[BMI][BF4] electrolyte has made it possible to observe the influence of temperature on the diffusion coefficient. The results show an increase in the diffusion coefficient with temperature, which highlights the importance of considering temperature in the design and modeling of electrochemical systems. This study also made it possible to set up a method to study the impact of temperature on diffusion in other electrolytes. These results could contribute to improve the understanding of electrochemical phenomena and to optimize the performance of electrochemical systems in many fields of application, such as energy storage, catalysis and green chemistry.\
However, it's worth mentioning that whilst simulation is a strong tool to examine physical systems, it only comes at the cost of physical correspondence. In other words, simulation is not duplication; one is a physical reality, the other is merely a series of flipping 1s and 0s on the level of CPU. Nevertheless, simulations can be useful when used as post-theoretic examination of physical systems that are often hard and/or expensive to simulate or when the technology is not there yet to study the system empirically. 







