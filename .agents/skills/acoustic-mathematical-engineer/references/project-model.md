# Project Model: Target-Frequency Geometric Acoustic Device

## 1. Project status

Status: Preliminary formulation under development.

Primary objective: Develop and validate a geometric and mathematical approach to acoustic attenuation or absorption, guided by measured target frequencies.

Implementation language: Python.

The physical mechanism and final geometric architecture have not yet been established.

## 2. Intended operating scenario

Application: Acoustic environments containing machinery or other sources with identifiable spectral components.

Source characterization:

- Source identity: To be documented.
- Operating conditions: To be documented.
- Target frequencies: To be measured or specified.
- Spectral variability: Unknown until characterized.
- Relevant receiver locations: To be defined.

Required acoustic outcome:

- Metric: To be specified.
- Target frequency range: To be specified.
- Required performance: To be specified.
- Installation constraints: To be specified.

## 3. Proposed physical hypothesis

Working hypothesis:

A geometry designed around target frequencies may alter acoustic propagation through internal reflections, phase relationships, interference, resonant behavior or other geometry-dependent mechanisms.

The proposed device may seek to confine acoustic energy and increase internal interactions, potentially enabling energy dissipation.

The relationship between these phenomena and net acoustic absorption remains to be established.

The proposed role of rapid beats, phase opposition and heat generation is an open hypothesis requiring a physical model and independent validation.

## 4. Mathematical formulation

Version: 0.1 — initial documented formulation.

### Definitions

Current variables and parameters in code:
- $f$: Target acoustic frequency [Hz]
- $c$: Speed of sound in medium [m/s]
- $\lambda = c / f$: Fundamental acoustic wavelength [m]
- $n \in \mathbb{N}_0$: Harmonic division order ($D_{\text{ref}} = \lambda / 2^n$) [dimensionless]
- $k \ge 1$: Fractal opening iteration order [dimensionless]
- $D_c, R_c$: Diameter and radius of circumscribed sphere [m]
- $D_i, R_i$: Diameter and radius of inscribed sphere [m]
- $a$: Polyhedron edge length [m]
- $H$: Overall characteristic height/dimension [m]
- $S$: Total nominal surface area [$m^2$]
- $V$: Enclosed cavity volume [$m^3$]
- $S/V$: Specific surface-to-volume ratio [$m^{-1}$]
- $\theta$: Dihedral angle between adjacent faces [degrees]
- $\Psi$: Wadell sphericity index [dimensionless]
- $a_k$: Subdivided fractal opening edge length [m]
- $N_{f,k}, N_{\text{tot},k}$: Number of openings per face and total per polyhedron
- $A_{\text{tot},k}$: Total perforated area [$m^2$]
- $P_{\text{tot},k}$: Total wetted perimeter of openings [m]
- $\sigma = A_{\text{tot},k} / S$: Surface porosity / perforation ratio [dimensionless]
- $\delta_v = \sqrt{2\mu / (\rho_0 \omega)}$: Viscous boundary layer thickness [m]
- $r_h = 2A/P$: Hydraulic radius of opening [m]
- $s = r_h / \delta_v$: Womersley / Stokes shear parameter [dimensionless]

### Governing equations

1. **Wavelength**:
   $$\lambda = \frac{c}{f}$$
2. **Inscribed Polyhedron Surface-to-Volume Theorem**:
   $$\frac{S}{V} = \frac{3}{R_i} = \frac{6}{D_i}$$
3. **Fractal Opening Edge Scaling**:
   - Triangles: $a_k = a / 2^k, \quad N_{f,k} = 3^{k-1}$
   - Squares: $a_k = a / 3^k, \quad N_{f,k} = 8^{k-1}$
   - Pentagons: $a_k = a / \phi^{2k}, \quad N_{f,k} = 5^{k-1}$
4. **Perimeter Divergence Relation**:
   $$P_{\text{tot},k} \propto \left(\frac{3}{2}\right)^k \to \infty, \quad \frac{P_{\text{tot},k}}{A_{\text{tot},k}} \propto 2^k \to \infty$$

## 5. Python implementation

Repository: `/home/mintmzu/MyRepos/CalcoliMatematicaAcustica`

Core geometry module: `geometria_solidi.py`

Acoustic thermodynamics and wave kinematic module: `acustica.py`

Fractal aperture module: `frattali_aperture.py`

Main calculation and reporting CLI: `calcolatore.py`

Tests:
- `test_matematica.py` (geometric and bidirectional inverse consistency)
- `test_frattali.py` (scaling law and boundary layer parameters)

## 6. Competing physical explanations & State-of-the-Art Trapping Models

Candidate explanations and established wave-trapping analogues:

1. **Acoustic Black Holes (ABH)**:
   - *Trap Mechanism*: Retardation through power-law thickness/impedance gradient ($c_p \to 0, \lambda \to 0$).
   - *Loss Mechanism*: Viscoelastic layer at the truncated tip.
   - *Distinction from our model*: ABH requires a continuous 1D smooth gradient. Our model uses a 3D polyhedral cavity with discrete fractal boundary openings.

2. **Space-Coiling (Labyrinthine Metamaterials)**:
   - *Trap Mechanism*: Path extension through coiled sub-wavelength channels ($L_{\text{eff}} \gg L_{\text{geom}}, n_{\text{eff}} \gg 1$).
   - *Loss Mechanism*: Viscous and thermal losses along the channel boundaries.
   - *Distinction from our model*: Space-coiling forces sound through folded 1D/2D ducts. Our model uses a full 3D cavity with non-orthogonal boundary reflections ($70.53^\circ$) and 2D surface fractal perforations.

3. **Quasi-Bound States in the Continuum (Quasi-BIC)**:
   - *Trap Mechanism*: Destructive interference of leakage channels into the radiation continuum ($Q_{\text{rad}} \to \infty$).
   - *Loss Mechanism*: Massive internal dwell-time amplification enabling complete dissipation through small intrinsic wall/fluid losses ($1/Q_{\text{int}}$).
   - *Distinction from our model*: Quasi-BIC relies on delicate destructive interference of radiating channels. Our model investigates whether multi-scale self-similar apertures (Sierpinski order $k$) can create impedance matching without single-frequency hypersensitivity.

4. **Other Baseline Phenomena to Disentangle**:
   - Geometric redirection / spatial scattering of acoustic energy
   - Standing wave formation and modal spatial interference
   - Viscous shear losses in boundary layers of fractal apertures ($\delta_v = \sqrt{2\mu / (\rho_0 \omega)}$)
   - Structural wall damping (if elastic walls are used)

## 7. Verification ledger

| Claim | Evidence required | Current status |
| --- | --- | --- |
| Geometry is mathematically valid | Geometric invariants and edge-case tests | Verified ($|\Delta| < 10^{-15}$) |
| Python code implements the intended equations | Equation-to-code audit | Verified |
| Target frequencies predict useful geometric parameters | Explicit model and independent checks | Open (Hypothesis) |
| Internal reflections or confinement occur as predicted | Field calculation or measurement | Open |
| Proposed phase behavior occurs | Phase-resolved analysis or measurement | Open |
| Net acoustic energy is dissipated | Appropriate energy balance and loss model | Open |
| Heat generation is attributable to the proposed mechanism | Controlled thermal and energy measurements | Open |
| Device meets its acoustic objective | Defined metric and controlled comparison | Open |
| Results are robust to construction and installation | Tolerance and sensitivity analysis | Open |

## 8. Decisions and changes

- **2026-10-29 (Initial Baseline)**: Removed legacy disordered scripts. Implemented clean analytical modules `acustica.py`, `geometria_solidi.py`, `frattali_aperture.py`, `calcolatore.py`. Established bidirectional exact geometric inversions. Documented perimeter scaling law for fractal apertures.

## 9. Current open questions

1. What wave equation or numerical field solver models the sound field inside the polyhedral cavity with fractal openings?
2. What is the normal-incidence acoustic surface impedance $Z_{\text{in}}(f)$ and corresponding absorption coefficient $\alpha(f)$?
3. How does the non-orthogonal internal geometry (e.g. $70.53^\circ$ dihedral angle of the tetrahedron) modify modal decay rates compared to orthogonal cubical geometries?
4. What controlled impedance-tube (Kundt tube) experiment will test the real dissipation of the 3D-printed cell?
