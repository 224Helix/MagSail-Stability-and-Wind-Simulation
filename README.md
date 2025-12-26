# Stability and Control of MagSail-Equipped Spacecraft in Chaotic Wolf–Rayet Stellar Winds

## Research Question

What distances are relevant for a spacecraft with a MagSail near a Wolf-Rayet star? At what distances can the MagSail spacecraft maintain directional control with confidence?

The Wolf-Rayet star's properties are critical. We need to determine under what conditions the spacecraft can use stellar wind for steering and directional control.

This research addresses when a MagSail spacecraft can maintain stable flight and steer effectively using Wolf-Rayet stellar winds.

---

## Motivation

Magnetic sails (MagSails) enable spacecraft propulsion without propellant by leveraging stellar wind momentum. While previous studies have examined MagSail performance in steady stellar environments, behavior in highly variable winds—such as those from Wolf-Rayet stars with strong, turbulent outflows—remains poorly understood.

Wolf-Rayet winds present an extreme but valuable test case for MagSail stability and control authority. These winds feature high density, supersonic velocities, embedded magnetic fields, and significant turbulence. Understanding MagSail dynamics in such environments requires simplified yet physically realistic models to avoid prohibitive computational costs.

---

## Modeling Framework and Assumptions

### Stellar Wind Model

The stellar wind incorporates:

- Hydrodynamic base flow matching WR wind characteristics
- Embedded turbulent eddies and shock structures
- Three fundamental MHD wave modes (Alfvén, fast, and slow magnetosonic)
- Observationally constrained WR wind parameters with controlled spatiotemporal variability

Wind evolution uses a modified Taylor frozen-flow approximation with temporal modulation functions, allowing turbulent structures to advect while remaining dynamically active.

### Magnetic Coupling Approximation

The spacecraft experiences forces and torques from the stellar wind's magnetic field structure. The one-way coupling approximation assumes:

- Stellar wind magnetic structure remains unaffected by spacecraft fields
- Small sail cross-sections justify neglecting wind perturbations
- Eliminates the need for full MHD simulations, enabling efficient parametric exploration

---

## Spacecraft Configuration and Dynamics

The spacecraft configuration includes:

- One primary MagSail for propulsion and momentum exchange
- Three secondary magnetic sails for torque and steering authority

Analysis focuses on dynamical stability and control feasibility rather than material properties or structural details.

---

## Stability and Control Metrics

Stability is quantified through probabilistic analysis across varying wind conditions:

- **Attitude deviation**: Maximum deviation from nominal orientation
- **Trajectory divergence rates**: Divergence between trajectories
- **Bounded motion probability**: Probability of maintaining motion within predefined thresholds
- **Certainty**: Probability of sustained stability at specific distances from the star

---

## Expected Outcomes and Scope

Primary outputs include:

- Distance-dependent stability regimes for MagSail spacecraft in chaotic WR winds
- Quantitative confidence thresholds for sustained stabilization
- Controlled wind-assisted steering regions
- Clear delineation of failure modes and kinematic approximation limitations

This work emphasizes MagSail dynamics in extreme stellar environments without attempting full plasma feedback modeling.

---

## Significance

By explicitly constraining physical assumptions and the modeling regime, this study provides a systematic framework for evaluating MagSail feasibility under realistic stellar wind variability. Results are relevant to theoretical studies, computational modeling, and understanding magnetically mediated spacecraft dynamics in astrophysical plasmas.

### Documentation 

## Project Structure
```
magsail-wr-stability/
│
├── src/
|   ├── integrator.py          # Integrator and main file
│   │
│   ├── config.py          # Sail geometries/inertia tensors
│   │
│   ├── wind/
│   │   ├── turbulence.py      # Spectral field generation
│   │   ├── evolution.py       # Modified Taylor frozen flow
│   │   └── wr_params.py       # WR 140 physical parameters
│   │
│   ├── spacecraft/
│   │   ├── dynamics.py        # 6DOF equations of motion
│   │   └── magsail.py         # Magnetic sail physics
│   │
│   ├── coupling/
│   │   ├── forces.py          # Wind → sail force calculation
│   │   └── torques.py         # Wind → sail torque calculation
│   │
│   ├── simulation/
│   │   ├── monte_carlo.py     # MC loop wrapper
│   │   └── stability.py       # Stability metrics
│   │
│   └── utils/
│       ├── visualization.py   # Plotting functions
│       ├── validation.py      # Model validation checks
│       └── io.py              # Save/load data
│
├── tests/
│   ├── test_wind.py           # Unit tests for wind model
│   ├── test_dynamics.py      
│
├── notebooks/
│   ├── wind_validation.ipynb  # Compare to WR observations
│   ├── exploration.ipynb      # Quick experiments
│   └── figures.ipynb          # Generate paper figures
│
├── data/
│   ├── raw/                   # Observational data
│   ├── generated/             # Wind realizations
│   └── results/               # Simulation outputs
│
├── docs/
│   ├── approximations.md      # Document your approximations
│   └── equations.md           # Key equations reference
│
├── config/
│   └── params.yaml            # Simulation parameters
│
├── requirements.txt
└── README.md
```
